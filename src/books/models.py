from django.db import models

class Autors(models.Model):
    first_name = models.CharField(
        verbose_name = "First name",
        max_length=30,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name = "Last name",
        max_length=30,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        verbose_name = "Autor's date of birth",
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    address = models.ForeignKey(
        'Addresses',
        verbose_name = "Autor's address",
        on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'

    def __str__(self):
        return F"{self.first_name} {self.last_name}"

class Addresses(models.Model):
    city = models.ForeignKey(
        'Cities',
        verbose_name = "City",
        on_delete=models.DO_NOTHING
    )

    street = models.TextField(
        verbose_name = "Street's name",
        max_length=100
    )

    block = models.PositiveSmallIntegerField(
        verbose_name = "Block's name"
    )

    house = models.PositiveSmallIntegerField(
        verbose_name = "Number of house"
    )

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return F"{self.city} {self.street} {self.block} / {self.house}"

class Cities(models.Model):
    name = models.CharField(
        verbose_name = "City's name",
        max_length=50
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(
        verbose_name = "Genre's name",
        max_length=50
    )

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

class Publishers(models.Model):
    name = models.CharField(
        verbose_name = "Publisher's name",
        max_length=50
    )
    address = models.ForeignKey(
        'Addresses',
        verbose_name = "Autor's address",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name
