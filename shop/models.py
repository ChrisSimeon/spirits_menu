from dataclasses import Field
from doctest import debug_script
from email.mime import image
from django.db import models
from django.utils.translation import gettext_lazy as _
import json

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200, default="", unique=True)
    description = models.TextField(default="", null=True, blank=True)
    show= models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Kategorie')
        verbose_name_plural= _("Kategorien")
    
    @classmethod
    def get_default_pk(cls):
        category, created = cls.objects.get_or_create(
            name='Sonstiges', description='Alles Weitere', show=False)
        return category.pk
    
    
class SubCategories(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="", null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_DEFAULT, null = True, default=Categories.get_default_pk)
    show= models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Unterkategorie')
        verbose_name_plural= _("Unterkategorien")
        
    @classmethod
    def get_default_pk(cls):
        subcategory, created = cls.objects.get_or_create(
            name='Sonstiges', description='Alles Weitere', show=False)
        return subcategory.pk


class Products(models.Model):
    name = models.CharField(max_length=200, default="")
    category=models.ForeignKey(Categories, models.SET_DEFAULT, blank=False, default=Categories.get_default_pk)
    subcategory = models.ForeignKey(SubCategories,models.SET_DEFAULT,blank=True,null=True, default=SubCategories.get_default_pk)
    prozent = models.IntegerField(null = True)
    description = models.TextField(default="", null=True, blank=True)
    availability = models.BooleanField(default=True)
    image = models.FileField(upload_to='', blank=True,null=True)
    price1 = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    price2 = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Produkt')
        verbose_name_plural= _("Produkte")


class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural= _("Tags")


class Cocktails(models.Model):
    name = models.CharField(max_length=200, default="")
    description= models.TextField(blank=True)
    image= models.FileField(upload_to='', blank=True)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    tags = models.ManyToManyField(Tags, blank=True)
    ingredients = models.ManyToManyField(Products, blank=True)
    recommendations = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Cocktail')
        verbose_name_plural= _("Cocktails")  
    

