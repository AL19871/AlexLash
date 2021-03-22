from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        null=True,
        blank=False
    )

    date_of_create = models.DateField(
        verbose_name = "Date of create",
        auto_now=False,
        auto_now_add=True
    )

    date_of_update = models.DateField(
        verbose_name = "Date of update",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return f'cart #{self.pk}'

    @property
    def total_summ(self):
        books_in_cart_all = self.booksincart.all()
        total = 0
        for obj_item in books_in_cart_all:
            total += obj_item.total_summ
        return total

class BookInCart(models.Model):
    cart = models.ForeignKey(
        'Cart',
        related_name='booksincart',
        on_delete=models.CASCADE,
    )
    
    book = models.ForeignKey(
        'books.BooksList',
        verbose_name='Book in a cart',
        on_delete=models.PROTECT
    )

    quantity = models.SmallIntegerField(
        verbose_name='Quantity',
        default=1
    )

    price = models.DecimalField(
        verbose_name='Price',
        max_digits=15,
        decimal_places=2
    )

    date_of_create = models.DateField(
        verbose_name = "Date of create",
        auto_now=False,
        auto_now_add=True
    )

    date_of_update = models.DateField(
        verbose_name = "Date of update",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return f'Book in a cart: #{self.pk} {self.book.name} quantity: {self.quantity} price: {self.price}'

    @property
    def total_summ(self):
        return self.price * self.quantity