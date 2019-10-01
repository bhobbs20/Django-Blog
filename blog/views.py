from django.shortcuts import render

def inex(request):
    return render(request, 'blog/index.html')
