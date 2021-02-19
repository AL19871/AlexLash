from django.db import models

class Autors(models.Model):
    first_name = models.CharField(
        verbose_name = "Autor's first name",
        max_length=30
    )
    last_name = models.CharField(
        verbose_name = "Autor's last name",
        max_length=30
    )
    date_of_birth = models.DateField(
        verbose_name = "Autor's date of birth",
        auto_now=False,
        auto_now_add=False
    )

    address = models.ForeignKey(
        'books.Addresses',
        verbose_name = "Autor's address",
        on_delete=models.DO_NOTHING,
        related_name = 'autors',
        null = True,
        blank = True
    )

    description = models.TextField(
        verbose_name = "Author's description",
        max_length = 256,
        blank = True
    )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'

    def __str__(self):
        return F"{self.first_name} {self.last_name}"

class Addresses(models.Model):
    city = models.ForeignKey(
        'books.Cities',
        verbose_name = "City",
        on_delete=models.DO_NOTHING,
        related_name = 'addresses'
    )

    street = models.TextField(
        verbose_name = "Street's name",
        max_length=100
    )

    block = models.PositiveSmallIntegerField(
        verbose_name = "Block's name",
        null = True,
        blank = True
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
        max_length = 50
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(
        verbose_name = "Genre's name",
        max_length = 50
    )
    description = models.TextField(
        verbose_name = "Genre's description",
        max_length = 256,
        blank = True
    )

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(
        verbose_name = "Seria's name",
        max_length=50
    )
    description = models.TextField(
        verbose_name = "Seria's description",
        max_length = 256,
        blank = True
    )

    class Meta:
        verbose_name = 'Seria'
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.name

class Publishers(models.Model):
    name = models.CharField(
        verbose_name = "Publisher's name",
        max_length=50
    )
    address = models.ForeignKey(
        'books.Addresses',
        verbose_name = "Publisher's address",
        on_delete = models.CASCADE,
        related_name = 'publishers',
        null = True,
        blank = True
    )
    description = models.TextField(
        verbose_name = "Publisher's description",
        max_length = 256,
        blank = True
    )

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name

class BooksList(models.Model):
    name = models.CharField(
        verbose_name = "Book's name",
        max_length = 100
    )

    image = models.ImageField(
        verbose_name = "Book's image",
        null = True,
        blank = True
    )

    cost = models.FloatField(
        verbose_name = "Book's cost",
    )

    author = models.ManyToManyField(Autors)

    seria = models.ForeignKey(
        'books.Series',
        verbose_name = "Book's seria",
        on_delete=models.DO_NOTHING,
        related_name = 'bookslistserie',
        null = True,
        blank = True
    )

    genre = models.ManyToManyField(Genres)

    year_of_publishing = models.PositiveSmallIntegerField(
        verbose_name = "Book's year of publishing",
        null = True,
        blank = True
    )

    number_of_pages = models.PositiveSmallIntegerField(
        verbose_name = "Book's number of pages",
        null = True,
        blank = True
    )

    BINDING_TYPES = (
        ('Solid', 'Solid'),
        ('Soft', 'Soft'),
    )

    binding = models.CharField(max_length=5,
        verbose_name = "Book's binding",
        choices = BINDING_TYPES,
        blank = True)

    FORMAT_TYPES = (
        ('Extra-large', 'Extra-large'),
        ('Large', 'Large'),
        ('Medium', 'Medium'),
        ('Small', 'Small'),
        ('Extra-small', 'Extra-small'),
    )

    format_of_book = models.CharField(max_length=15,
        verbose_name = "Book's format",
        choices = FORMAT_TYPES,
        blank = True)

    ISBN = models.CharField(
        verbose_name = "Book's ISBN",
        max_length = 100,
        blank = True
    )

    weight = models.PositiveSmallIntegerField(
        verbose_name = "Book's weight (gram)",
        null = True,
        blank = True
    )

    age_restrictions = models.PositiveSmallIntegerField(
        verbose_name = "Book's age restrictions",
        null = True,
        blank = True
    )

    publisher = models.ForeignKey(
        'books.Publishers',
        verbose_name = "Book's publisher",
        on_delete=models.DO_NOTHING,
        related_name = 'bookslistpublisher',
        null = True,
        blank = True
    )

    amount = models.PositiveSmallIntegerField(
        verbose_name = "Book's amount",
        null = True,
        blank = True
    )

    active = models.BooleanField(
        verbose_name = "Active"
    )

    RATING_TYPES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    rating = models.CharField(max_length=15,
        verbose_name = "Book's rating",
        choices = FORMAT_TYPES,
        null = True,
        blank = True)

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
        verbose_name = 'Book'
        verbose_name_plural = 'Books list'

    def __str__(self):
        return self.name