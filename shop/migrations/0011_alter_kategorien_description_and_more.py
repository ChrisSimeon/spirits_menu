# Generated by Django 4.0.2 on 2022-02-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_produkte_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorien',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='unterkategorien',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
