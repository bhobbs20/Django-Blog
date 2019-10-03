from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Post
from categories.models import Category




def index(request):
    posts = Post.objects.order_by('-created_date').filter(is_published=True)
    cats = Category.objects.all()
    popular_posts = [Post.objects.get(pk=1), Post.objects.get(pk=2), Post.objects.get(pk=3)]

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
   
    context = {
        'posts': paged_posts,
        'cats': cats,
        'popular_posts': popular_posts,
      
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')
