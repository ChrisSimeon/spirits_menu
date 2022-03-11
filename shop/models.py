from dataclasses import Field
from doctest import debug_script
from email.mime import image
from django.db import models
from django.utils.translation import gettext_lazy as _
import json

# Create your models here.

class Kategorien(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="", null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Kategorie')
        verbose_name_plural= _("Kategorien")
    
    
class UnterKategorien(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="", null=True, blank=True)
    categorie = models.ForeignKey(Kategorien, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Unterkategorie')
        verbose_name_plural= _("Unterkategorien")


class Produkte(models.Model):
    name = models.CharField(max_length=200, default="")
    categorie = models.ForeignKey(Kategorien, on_delete=models.CASCADE, null = True)
    subcategorie = models.ForeignKey(UnterKategorien,models.SET_NULL,blank=True,null=True)
    prozent = models.IntegerField(null = True)
    description = models.TextField(default="", null=True, blank=True)
    availability = models.BooleanField(default=False)
    image = models.FileField(upload_to='', blank=True,null=True)
    preis1 = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    preis2 = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Produkt')
        verbose_name_plural= _("Produkte")


class Cocktails(models.Model):
    # name = models.CharField(max_length=200, default="")
    # description= models.TextField(blank=True)
    # image= models.FileField(upload_to='', blank=True)
    # preis = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    # zutat1 = models.ForeignKey(null=True, blank=True)
    def __str__(self):
        return self.name
