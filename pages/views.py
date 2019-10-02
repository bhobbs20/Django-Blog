from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
    posts = Post.objects.order_by('-created_date').filter(is_published=True)
   
    context = {
        'posts': posts, 
    }

    return render(request, 'pages/index.html', context)

def about(request):
    context =  {}
    return render(request, 'pages/about.html')
