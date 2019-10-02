from django.contrib import admin
from .models import Post

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'text',  'author', 'main_photo')
    list_display_links =('id', 'title')
   
    list_editable = ('is_published', 'text', 'main_photo')
    # search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # list_per_page = 25





admin.site.register(Post, PostsAdmin)

