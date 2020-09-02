from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView
from . import forms
from . import models
from .models import User

from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
class CreateUser(CreateView):

    form_class = forms.UserCreateForm
    success_url = reverse_lazy("home")
    template_name = "accounts/create_user.html"

class UserListView(ListView):
    # context_object_name = 'myusers'
    model = models.User
