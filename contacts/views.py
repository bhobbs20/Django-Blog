from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact_pigeon(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    
    contact = Contact(name=name, email=email, subject=subject, message=message)

    contact.save()

  
    return redirect('index')
