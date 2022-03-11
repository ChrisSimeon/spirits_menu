from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Kategorien, UnterKategorien, Produkte
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.generic.detail import DetailView


# Create your views here.

def home(request):
    
    data = []
    for kategorie in Kategorien.objects.all():
        name = kategorie.name
        id = kategorie.id
        produkte = Produkte.objects.filter(categorie = kategorie)
        data.append([kategorie,produkte])
    context = {"context": data}
    return render(request, "shop/main.html", context)


def kategorienViews(request, *args, **kwargs):
    temp = kwargs["produkt"]
    try:
        Kategorie = Kategorien.objects.get(name='{}'.format(temp))
        produkte = Kategorie.produkte_set.all()
        context = {"produkte": produkte}
    except:
        context= {}

    return render(request, "shop/kategorien.html", context)


class spiritsDetailView(DetailView):
    model= Produkte
    template_name= "shop/detailView.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context