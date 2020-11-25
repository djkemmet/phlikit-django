from django.urls import path, include
from landing.views import update_MailinglistSignUp, thanks
from landing import views

urlpatterns = [
    path('', views.index, name="landing_index"),
    path('mailinglist/', views.update_MailinglistSignUp),
    path('thanks/', views.thanks),
]
