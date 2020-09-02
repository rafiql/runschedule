from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from .models import Client
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ClientListView(ListView):

    model = models.Client

class ClientCreateView(LoginRequiredMixin,CreateView):
    fields = ("name","email","mobile", "address")
    model = models.Client

    # redirect_field_name = 'clients/client_form.html'

    # form_class = PostForm
