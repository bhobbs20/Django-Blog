
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from .models import Post

def index(request):
    posts = Post.objects.order_by('-created_date').filter(is_published=True)
   
    context = {
        'posts': posts, 
    }

    return render(request, 'blogs/index.html', context)

def blog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
       'post': post
    }

    return render(request, 'blogs/blog.html', context)

