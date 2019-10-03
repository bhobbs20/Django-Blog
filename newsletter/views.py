from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsLetter


def newsletter(request):
  if request.method == 'POST':
    email = request.POST['email']
   
    newsletter = NewsLetter(email=email)
    newsletter.save()

    return redirect('index')