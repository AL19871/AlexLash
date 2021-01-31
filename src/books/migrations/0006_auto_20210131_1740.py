# Generated by Django 3.1.5 on 2021-01-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210131_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='publishers',
            options={'verbose_name': 'Publisher', 'verbose_name_plural': 'Publishers'},
        ),
        migrations.RemoveField(
            model_name='genres',
            name='age',
        ),
        migrations.RemoveField(
            model_name='publishers',
            name='age',
        ),
        migrations.AlterField(
            model_name='addresses',
            name='street',
            field=models.TextField(max_length=100, verbose_name="Street's name"),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=50, verbose_name="Genre's name"),
        ),
        migrations.AlterField(
            model_name='publishers',
            name='name',
            field=models.CharField(max_length=50, verbose_name="Publisher's name"),
        ),
    ]
