from django.contrib import admin
from .models import Image,Location,categories

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display =['name','location']

class LocationAdmin(admin. ModelAdmin):
    list_display = ['name']
    ordering = ['name']

class categoriesAdmin(admin. ModelAdmin):
    list_display = ['name']
    ordering = ['name']    

admin.site.register(Image, ImageAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(categories, categoriesAdmin)
