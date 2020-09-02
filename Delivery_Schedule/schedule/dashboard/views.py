from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def charts(request):
#     return render(request,'themeapp/charts.html')

class ChartsView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard/charts.html'
