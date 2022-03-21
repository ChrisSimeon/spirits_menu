from django.contrib import admin

# Register your models here.
from .models import Cocktails, Categories,SubCategories,Products, Tags

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(Cocktails)
admin.site.register(Tags)
