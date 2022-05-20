from django.contrib import admin
from .models import *


class StoreAdmin(admin.ModelAdmin):
    list_display = ['username' , 'password']

admin.site.register(Store , StoreAdmin)
admin.site.register(Category)
admin.site.register(Product)

