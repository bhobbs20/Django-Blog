from django.shortcuts import render, redirect
from django.contrib import messages
# from django.core.mail import send_mail
from .models import Contact


def index(request):
    return render(request, 'contacts/contact.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    
    contact = Contact(name=name, email=email, subject=subject, message=message)

    contact.save()

    messages.success(request, 'Your request has been submitted')
    return redirect('index')
