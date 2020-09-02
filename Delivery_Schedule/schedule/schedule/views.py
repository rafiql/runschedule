from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)
