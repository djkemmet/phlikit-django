from django.urls import path, include
from links.views import shorten
from links import views

urlpatterns = [
    path('shorten/', views.shorten),
    path('', views.root),    
]
