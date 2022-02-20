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


# Create your views here.

def home(request):
    produkte = Produkte.objects.all()
    context = {"Produkte" : produkte}
    print(produkte[1].image.url)
    return render(request, "shop/main.html", context)


class KategorienListe(LoginRequiredMixin,ListView):
    model = Kategorien
    template_name = "shop/kategorien.html"
    
class KategorienCreate(CreateView):
    model = Kategorien
    template_name = "shop/kategoriencreate.html"
    fields = ["name", "description"]
    
    
class SignUp (CreateView):
    form_class = UserCreationForm
    success_url= reverse_lazy("login")
    template_name = "registration/signup.html"
    
def logout_request(request):
    logout(request)
    return redirect("Shop")
        