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

@admin.register(ImageSettings)

class ImageSettingsAdmin(admin.ModelAdmin):
    list_display=['id','name','description','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['description','file']

    class Meta:
        model = ImageSettings

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=['id','order','name','percentage','updated_date','created_date']

    search_fields = ['name']
    list_editable=['order','name','percentage',]

    class Meta:
        model = Skill

    




        