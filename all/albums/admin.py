from django.contrib import admin
from .models import *


class PersonDataAdmin(admin.ModelAdmin):
    readonly_fields=('name',)
    
admin.site.register(Album,PersonDataAdmin)



