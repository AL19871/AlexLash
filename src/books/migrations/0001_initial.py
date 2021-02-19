# Generated by Django 3.1.5 on 2021-02-19 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(max_length=100, verbose_name="Street's name")),
                ('block', models.PositiveSmallIntegerField(verbose_name="Block's name")),
                ('house', models.PositiveSmallIntegerField(verbose_name='Number of house')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Autors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('date_of_birth', models.DateField(verbose_name="Autor's date of birth")),
                ('descpiption', models.TextField(max_length=256, verbose_name="Author's descpiption")),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='autors', to='books.addresses', verbose_name="Autor's address")),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autors',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="City's name")),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Genre's name")),
                ('descpiption', models.TextField(max_length=256, verbose_name="Genre's descpiption")),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Serie's name")),
                ('descpiption', models.TextField(max_length=256, verbose_name="Serie's descpiption")),
            ],
            options={
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Publisher's name")),
                ('descpiption', models.TextField(max_length=256, verbose_name="Publisher's descpiption")),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publishers', to='books.addresses', verbose_name="Publisher's address")),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.CreateModel(
            name='BooksList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Book's name")),
                ('image', models.ImageField(upload_to='', verbose_name="Book's image")),
                ('cost', models.FloatField(verbose_name="Book's cost")),
                ('year_of_publishing', models.PositiveSmallIntegerField(verbose_name="Book's year of publishing")),
                ('number_of_pages', models.PositiveSmallIntegerField(verbose_name="Book's number of pages")),
                ('binding', models.CharField(choices=[('Solid', 'Solid'), ('Soft', 'Soft')], max_length=5, verbose_name="Book's binding")),
                ('format_of_book', models.CharField(choices=[('Extra-large', 'Extra-large'), ('Large', 'Large'), ('Medium', 'Medium'), ('Small', 'Small'), ('Extra-small', 'Extra-small')], max_length=15, verbose_name="Book's format")),
                ('ISBN', models.CharField(max_length=100, verbose_name="Book's ISBN")),
                ('weight', models.PositiveSmallIntegerField(verbose_name="Book's weight (gram)")),
                ('age_restrictions', models.PositiveSmallIntegerField(verbose_name="Book's age restrictions")),
                ('amount', models.PositiveSmallIntegerField(verbose_name="Book's amount")),
                ('active', models.BooleanField(verbose_name='Active')),
                ('rating', models.CharField(choices=[('Extra-large', 'Extra-large'), ('Large', 'Large'), ('Medium', 'Medium'), ('Small', 'Small'), ('Extra-small', 'Extra-small')], max_length=15, verbose_name="Book's rating")),
                ('date_of_create', models.DateField(auto_now_add=True, verbose_name='Date of create')),
                ('date_of_update', models.DateField(auto_now=True, verbose_name='Date of update')),
                ('author', models.ManyToManyField(to='books.Autors')),
                ('genre', models.ManyToManyField(to='books.Genres')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookslistpublisher', to='books.publishers', verbose_name="Book's publisher")),
                ('seria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookslistserie', to='books.series', verbose_name="Book's serie")),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books list',
            },
        ),
        migrations.AddField(
            model_name='addresses',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='addresses', to='books.cities', verbose_name='City'),
        ),
    ]
