from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('list',views.ClientListView.as_view(),name='list'),
    path('creatcl/',views.ClientCreateView.as_view(),name='creatcl'),
]
