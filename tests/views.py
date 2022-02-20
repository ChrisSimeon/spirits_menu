from logging import raiseExceptions
from django.http import request
from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from tests.models import Owner
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def index(request):
    return render(request, "tests/index.html", {} )

class OwnerList(LoginRequiredMixin, ListView):
    model = Owner
    template_name= "tests/owner_list.html"

class OwnerCreate(CreateView):
    model = Owner
    template_name = "tests/owner_create_form.html"
    fields = ["first_name", "last_name", "phone"]
    def get_success_url(self):
        return reverse("owner_list")
    
class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "tests/owner_update.html"
    fields = ["first_name", "last_name", "phone"]
    def get_success_url(self):
        return reverse("owner_list")


class OwnerDelete (DeleteView):
  model = Owner
  template_name = "tests/owner_delete.html"
  def get_success_url(self):
      return reverse("owner_list")