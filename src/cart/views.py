from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, RedirectView
from . import models
from books import models as book_models
from . import utils
from books import utils as book_utils


class DetailCart(DetailView):
    model = models.Cart

    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        current_cart = utils.get_create_current_cart(self)
        if book_id:
            book = book_models.BooksList.objects.get(pk=book_id)
            book_in_cart, create_book_in_cart = models.BookInCart.objects.get_or_create(
                cart=current_cart,
                book=book,
                defaults={'quantity': 1, 'price': book.cost}
            )
            if not create_book_in_cart:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        book_utils.edit_context(self.request, context)

        obj_cart = utils.get_create_current_cart(self)

        context['book_list'] = obj_cart.booksincart.all().order_by(self.get_ordering())

        return context

    def get_ordering(self, *args, **kwargs):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()


class RecalculateCart(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        action = None
        return_urls = {'checkout': reverse('order:checkout')}
        current_cart_pk = self.request.session.get('current_cart_pk')
        if current_cart_pk:
            cart_items = self.request.GET
            action = utils.update_item_in_cart(cart_items, current_cart_pk)
        return return_urls.get(action, reverse('cart:add-to-cart'))