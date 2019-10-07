
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from .models import Post, Comment
from .forms import CommentForm
from categories.models import Category
from django.contrib.auth.models import User


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
    comments = Comment.objects.filter(post=post)
    popular_posts = [Post.objects.get(pk=1), Post.objects.get(pk=2), Post.objects.get(pk=3)]
    cats = Category.objects.all() 

   


    context = {
       'post': post,
       'cats': cats,
       'popular_posts': popular_posts,
        'comments': comments,
       
    }

    return render(request, 'blogs/blog.html', context)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        user = CommentForm(request.POST['user_id'])
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was posted, remember be nice!! :)')
            return redirect('blog', post.id)
    else:
        form = CommentForm()

    return render(request, 'blogs/add_comment_to_post.html', {'form': form})
