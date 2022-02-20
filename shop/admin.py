from django.contrib import admin

# Register your models here.
from .models import Kategorien,UnterKategorien,Produkte

admin.site.register(Kategorien)
admin.site.register(UnterKategorien)
admin.site.register(Produkte)
