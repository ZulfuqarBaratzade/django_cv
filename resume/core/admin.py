from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(General_Settings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameter','updated_date','created_date']
    search_fields = ['id','name']
    list_editable=['description','parameter']

    class Meta:
        model = General_Settings
    
