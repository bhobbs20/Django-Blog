from django.contrib import admin
from .models import Post, Comment

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'text',  'author', 'main_photo')
    list_display_links =('id', 'title')
    list_editable = ('is_published', 'text', 'main_photo')
   
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text','user_id',)
  
    
admin.site.register(Post, PostsAdmin)
admin.site.register(Comment, CommentsAdmin)

