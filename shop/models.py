from dataclasses import Field
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Kategorien(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Kategorie')
        verbose_name_plural= _("Kategorien")
    
    
class UnterKategorien(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
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
    description = models.TextField(default="")
    availability = models.BooleanField(default=False)
    image = models.FileField(upload_to='', blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Produkt')
        verbose_name_plural= _("Produkte")