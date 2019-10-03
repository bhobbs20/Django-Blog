from django.urls import path

from . import views

urlpatterns = [
  path('contact_pigeon', views.contact_pigeon, name='contact_pigeon')
]