# Generated by Django 4.0.2 on 2022-02-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_kategorien_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktails',
            name='preis',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='produkte',
            name='preis1',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='produkte',
            name='preis2',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]