from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:post_id>', views.blog, name='blog'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]