
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from .models import Post
from categories.models import Category


def index(request):
    posts = Post.objects.order_by('-created_date').filter(is_published=True)
    popular_posts = [Post.objects.get(pk=1), Post.objects.get(pk=2), Post.objects.get(pk=3)]
    
    context = {
        'posts': posts,
        'popular_posts': popular_posts,
    }

    return render(request, 'blogs/index.html', context)

def blog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    popular_posts = [Post.objects.get(pk=1), Post.objects.get(pk=2), Post.objects.get(pk=3)]
    cats = Category.objects.all() 
    context = {
       'post': post,
       'cats': cats,
       'popular_posts': popular_posts,
    }

    return render(request, 'blogs/blog.html', context)

