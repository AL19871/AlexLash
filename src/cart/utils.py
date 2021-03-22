from . import models


def get_create_current_cart(self, *args, **kwargs):

    current_customer = self.request.user

    if current_customer.is_anonymous:
        current_customer = None

    current_cart_id = self.request.session.get('current_cart_pk')

    current_cart, create_cart = models.Cart.objects.get_or_create(
        pk=current_cart_id,
        defaults={'customer': current_customer}
    )

    if create_cart:
        self.request.session['current_cart_pk'] = current_cart.pk
    
    return current_cart


def update_item_in_cart(cart_items, current_cart_pk):
    current_cart = models.Cart.objects.filter(pk=current_cart_pk).first()
    action = None

    if current_cart:
    
        goods = current_cart.booksincart.all()

        for item_id, quantity in cart_items.items():
            if item_id == 'btn':
                action = quantity
                continue
            good = goods.filter(pk=item_id).first()
            if good and int(quantity) > 0:
                good.quantity = quantity
                good.save()
            else:
                good.delete()
    
    return action