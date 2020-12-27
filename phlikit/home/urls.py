from django.urls import path, include
from home.views import user_home
from home import views

urlpatterns = [
    path('', views.user_home, name="landing_index"),
]
