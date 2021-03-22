from django.db import models

class Order(models.Model):
    cart = models.OneToOneField(
        'cart.Cart',
        verbose_name='Cart',
        on_delete=models.PROTECT
    )

    address = models.TextField(
        verbose_name='Address',
        null=True
    )

    phone = models.TextField(
        verbose_name='Phone',
        null=True
    )

    STATUS_TYPES = (
        ('Submitted', 'Submitted'),
        ('Canceled', 'Canceled'),
        ('Finished', 'Finished')
    )

    status = models.CharField(max_length=30,
        verbose_name = "Status",
        choices = STATUS_TYPES
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

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'order #{self.pk}'

    @property
    def total_summ(self):
        books_in_cart_all = self.cart.booksincart.all()
        total = 0
        for obj_item in books_in_cart_all:
            total += obj_item.total_summ
        return total