from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False
    )

    phone = models.CharField(
        verbose_name='Phone',
        max_length=13,
        blank=True,
        null=True
    )

    country = models.CharField(
        verbose_name='Country',
        max_length=100,
        blank=True,
        null=True,
        default=' '
    )

    city = models.CharField(
        verbose_name='City',
        max_length=100,
        blank=True,
        null=True,
        default=' '
    )

    postcode = models.CharField(
        verbose_name='Postcode',
        max_length=6,
        blank=True,
        null=True,
        default=' '
    )

    address1 = models.CharField(
        verbose_name='Address 1',
        max_length=150,
        blank=True,
        null=True,
        default=' '
    )

    address2 = models.CharField(
        verbose_name='Address 2',
        max_length=150,
        blank=True,
        null=True,
        default=' '
    )

    description = models.TextField(
        verbose_name='Description',
        max_length=150,
        blank=True,
        null=True,
        default=' '
    )

    def __str__(self):
        return f'user #{self.user}'