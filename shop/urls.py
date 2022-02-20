from django.urls import path, include
from . import views
from shop import views
from core import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views


urlpatterns = [
	path("", views.home, name="Shop"), 
	path("kategorien/", views.KategorienListe.as_view() , name="Kategorien"),
	path("kategoriencreate/", views.KategorienCreate.as_view() , name="KategorienCreate"),
	path("accounts/", include("django.contrib.auth.urls"), name="login"),
 	path("signup/", views.SignUp.as_view(), name="signup"),
 	path("logout/", views.logout_request, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
