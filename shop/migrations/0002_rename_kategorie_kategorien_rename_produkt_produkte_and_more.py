# Generated by Django 4.0.2 on 2022-02-08 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kategorie',
            new_name='Kategorien',
        ),
        migrations.RenameModel(
            old_name='Produkt',
            new_name='Produkte',
        ),
        migrations.RenameModel(
            old_name='SubCategories',
            new_name='UnterKategorien',
        ),
    ]