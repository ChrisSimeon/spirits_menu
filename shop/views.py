from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Categories, Products, SubCategories, Cocktails

# Create your views here.

def home(request):
    
    # for category in Categories.objects.all():
    #     if category["show"] == True:
    #         print(category)
            # for subcategory in category.subcategories_set.all():
            #     data[category][subcategory] = []
            #     for product in subcategory.products_set.all():
            #         data[category][subcategory].append(product)
    context = {
        
        "categories" : Categories.objects.all(),
        "subcategories": SubCategories.objects.all(),
        "products": Products.objects.all()  
        
    }
    return render(request, "shop/main.html", context)


def kategorienViews(request, *args, **kwargs):
    temp = kwargs["produkt"]
    try:
        Kategorie = Categories.objects.get(name='{}'.format(temp))
        produkte = Kategorie.produkte_set.all()
        context = {"produkte": produkte}
    except:
        context= {}

    return render(request, "shop/kategorien.html", context)


class spiritsDetailView(DetailView):
    model= Products
    template_name= "shop/detailView.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class cocktailsListView(ListView):
    model= Cocktails
    template_name= "shop/cocktails_main.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    

class cocktailsDetailView(DetailView):
    model= Cocktails
    template_name= "shop/cocktails_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context