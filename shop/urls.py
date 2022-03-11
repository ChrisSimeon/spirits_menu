from django.urls import path, include
from . import views
from shop import views
from core import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views


urlpatterns = [
	path("", views.home, name="Shop"), 
	path("kategorien/whisky", views.kategorienViews, {'produkt':'Whisky'}, name="KategorieWhisky"),
	path("kategorien/gin", views.kategorienViews, {'produkt':'Gin'}, name="KategorieGin"),
	path("kategorien/portwein", views.kategorienViews, {'produkt':'Portwein'}, name="KategoriePortwein"),
	path("kategorien/vodka", views.kategorienViews, {'produkt':'Vodka'}, name="KategorieVodka"),
	path("kategorien/wermut", views.kategorienViews, {'produkt':'Wermut'}, name="KategorieWermut"),
	path("spirits/<pk>", views.spiritsDetailView.as_view(), name="spiritsDetail"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
