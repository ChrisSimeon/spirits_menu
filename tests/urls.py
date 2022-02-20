from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"), # Das bedeutet bei keinen weiteren Argumenten soll die Index Funktion gerendert werden
    path("owner_list/", views.OwnerList.as_view() , name="owner_list"),
    path("owner_create/", views.OwnerCreate.as_view() , name="owner_create"),
    path("owner_update/<pk>", views.OwnerUpdate.as_view() , name="owner_update"),
    path("owner_delete/<pk>", views.OwnerDelete.as_view() , name="owner_delete"),
]