from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('charts/', views.ChartsView.as_view(), name="charts"),
]
