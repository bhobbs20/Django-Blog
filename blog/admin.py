from django.contrib import admin
from .models import Post, Category

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'text',  'author', 'main_photo')
    list_display_links =('id', 'title')
    list_filter = ('categories',)
    list_editable = ('is_published', 'text', 'main_photo')
    # search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # list_per_page = 25


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links =('id', 'name')
    list_filter = ('name',)


admin.site.register(Post, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
