# Generated by Django 3.1.5 on 2021-01-31 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210131_1050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addresses',
            new_name='Address',
        ),
    ]
