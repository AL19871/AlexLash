from django.shortcuts import render
from . import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, CreateView, UpdateView, DeleteView
from . import utils
from order import models as order_models
from books import utils as book_utils
from . import models
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

class UserProfileView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = models.UserProfile
    template_name = 'customer/userprofile_detail.html'
    fields = ('country', 'city', 'phone', 'postcode', 'address1', 'address2', 'description')

    def get_object(self, *args, **kwargs):
        
        if not self.request.user.is_authenticated:
            return

        user_customer = self.request.user
        
        current_customer, create_customer = models.UserProfile.objects.get_or_create(
                user=user_customer,
            )

        return current_customer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        user_customer = self.request.user

        context['permission_edit'] = self.request.user.has_perm('order.change_order')
        context['permission_delete'] = self.request.user.has_perm('order.delete_order')
        context['userprofile_order_list'] = order_models.Order.objects.filter(cart__customer=user_customer).all()

        book_utils.edit_context(self.request, context)

        return context


class SubmitCustomer(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('my-login')

    def get_redirect_url(self, *args, **kwargs):

        action_update = self.request.GET.get('btn_update')
        action_cancel = self.request.GET.get('btn_cancel')
        action_finish = self.request.GET.get('btn_finish')
        action_delete = self.request.GET.get('btn_delete')
        action_save = self.request.GET.get('btn_save')

        if action_update:

            self.request.session['current_order_pk'] = action_update

            return reverse('order:checkout')

        elif action_finish:

            current_order = order_models.Order.objects.filter(pk=action_finish).first()
            if current_order:

                current_order.status = 'Finished'
                current_order.save()

            return reverse('customer:profile')

        if action_delete:

            current_order = order_models.Order.objects.filter(pk=action_delete).first()
            if current_order:

                current_order.delete()

            return reverse('customer:profile')

        elif action_cancel:

            current_order = order_models.Order.objects.filter(pk=action_cancel).first()
            if current_order:

                current_order.status = 'Canceled'
                current_order.save()

            return reverse('customer:profile')

        elif action_save:

            user_customer = models.UserProfile.objects.filter(user=self.request.user).first()

            if user_customer and action_save == 'submit':
                customer_items = self.request.GET
                utils.update_customer(user_customer, customer_items)

            return reverse('home-page')

        return reverse('home-page')


class RegistrationView(CreateView):
    template_name = 'customer/register.html'
    form_class = forms.UserDetailsForm
    success_url = reverse_lazy('customer:profile')
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        auth_user.groups.add(Group.objects.get(name='Customers'))
        login(self.request, auth_user)
        return form_valid

class UserProfileList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = models.UserProfile
    permission_required = ('customer.view_userprofile', 'customer.change_userprofile')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context = book_utils.edit_context(self.request, context)
        return context

class UserProfileUpdateManager(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = models.UserProfile
    template_name = 'customer/userprofile_update.html'
    fields = ('city', 'country', 'phone', 'postcode', 'address1', 'address2')
    permission_required = ('customer.view_userprofile', 'customer.change_userprofile')
    success_url = reverse_lazy('customer:profile-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['permission'] = self.request.user.has_perm('customer.change_userprofile')
        context = book_utils.edit_context(self.request, context)
        return context

class UserProfileDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = models.UserProfile
    permission_required = 'customer.delete_userprofile'
    success_url = reverse_lazy('customer:profile-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['permission'] = self.request.user.has_perm('order.delete_order')
        context = book_utils.edit_context(self.request, context)
        return context