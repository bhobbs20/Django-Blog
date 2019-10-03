from django.contrib import admin
from .models import Contact


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message',)
   

admin.site.register(Contact, ContactsAdmin)

