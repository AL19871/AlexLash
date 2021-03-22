from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, RedirectView, ListView, UpdateView, DeleteView
from . import models
from . import utils
from cart import utils as cart_utils
from cart import models as cart_models
from order import utils as order_utils
from books import utils as book_utils
from customer import models as cutomer_models
from django.db.models import Q


class DetailOrder(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = models.Order
    template_name = 'order/order_detail.html'
    fields = ('address', 'phone')

    def get_object(self, *args, **kwargs):

        current_order_id = self.request.session.get('current_order_pk')

        if current_order_id:
            current_order = models.Order.objects.filter(pk=current_order_id).first()
        else:
            current_cart = cart_utils.get_create_current_cart(self)
            if current_cart:
                current_user = self.request.user
                if current_user != current_cart.customer:
                    current_cart.customer = current_user
                    current_cart.save()
                if current_user.is_authenticated:
                    user_customer = cutomer_models.UserProfile.objects.filter(user=self.request.user).first()
                    if user_customer:
                        current_order, create_order = models.Order.objects.get_or_create(
                            cart=current_cart,
                            defaults={'address': user_customer.address1, 'phone': user_customer.phone}
                        )
                    else:
                        return
                else:
                    current_order, create_order = models.Order.objects.get_or_create(
                        cart=current_cart
                    )
        return current_order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        book_utils.edit_context(self.request, context)

        current_order_id = self.request.session.get('current_order_pk')
        if current_order_id:
            obj_cart = models.Order.objects.filter(pk=current_order_id).first().cart
        else:
            obj_cart = cart_utils.get_create_current_cart(self)

        context['book_list'] = obj_cart.booksincart.all().order_by(self.get_ordering())

        return context

    def get_ordering(self, *args, **kwargs):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()


class SubmitOrder(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('my-login')
    def get_redirect_url(self, *args, **kwargs):

        order_submit = self.request.GET.get('btn')
        address_order = self.request.GET.get('address')
        phone_order = self.request.GET.get('phone')

        if not address_order or address_order == '' or not phone_order or phone_order == '':
            return reverse('order:checkout')

        current_order_id = self.request.session.get('current_order_pk')

        if current_order_id:
            current_order = models.Order.objects.filter(pk=current_order_id).first()
            order_utils.update_order(current_order, address_order, phone_order, order_submit)
            
            self.request.session['current_order_pk'] = None

            return reverse('customer:profile')

        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                
                current_cart = cart_models.Cart.objects.filter(pk=current_cart_pk).first()
    
                if current_cart:
                    current_order = models.Order.objects.filter(cart=current_cart).first()
                    order_utils.update_order(current_order, address_order, phone_order, order_submit, True)
                    if order_submit == 'submit':
                        self.request.session['current_cart_pk'] = None
        return reverse('home-page')


class OrdersList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    paginate_by = 10
    model = models.Order
    permission_required = 'order.view_order'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['permission_view'] = self.request.user.has_perm('order.view_order')
        context['permission_delete'] = self.request.user.has_perm('order.delete_order')
        context['permission_change'] = self.request.user.has_perm('order.change_order')
        context['search_field'] = 'order:order-list'
        book_utils.edit_context(self.request, context)

        return context

    def get_ordering(self, *args, **kwargs):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(address__icontains=field_to_query) | Q(phone__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs


class OrderDetailView(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = models.Order
    template_name = 'order/order_detail_admin.html'
    permission_required = ('order.view_order', 'order.change_order')
    success_url = reverse_lazy('order:order-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('order.change_order')
        context = book_utils.edit_context(self.request, context)
        return context


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = models.Order
    template_name = 'order/order_update.html'
    fields = ('address', 'phone', 'status')
    permission_required = 'order.view_order'
    success_url = reverse_lazy('order:order-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('order.view_order')
        context = book_utils.edit_context(self.request, context)
        return context

class OrderDeleteView(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = models.Order
    redirect_field_name = 'redirect_to'
    permission_required = ('order.view_order', 'order.delete_order')
    success_url = reverse_lazy('order:order-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('order.delete_order')
        context = book_utils.edit_context(self.request, context)
        return context
