from django.contrib import admin
from .models import NewsLetter


class NewsLettersAdmin(admin.ModelAdmin):
    list_display = ( 'email',)
   

admin.site.register(NewsLetter, NewsLettersAdmin)
