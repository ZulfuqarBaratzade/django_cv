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

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=['id','company_name','job_title','job_location','start_date','end_date']

    search_fields = ['company_name','job_title','job_location']
    list_editable=['company_name','job_title','job_location','start_date','end_date']

    class Meta:
        model = Experience

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=['id','edu_name','edu_title','edu_location','start_date','end_date']

    search_fields = ['edu_name','edu_title','edu_location']
    list_editable=['edu_name','edu_title','edu_location','start_date','end_date']

    class Meta:
        model = Experience
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display=['id','order','link','icon','updated_date','created_date']

    search_fields = ['order','link','icon']
    list_editable=['link','icon',]

    class Meta:
        model = SocialMedia
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display=['id','slug','file','button_text','updated_date','created_date']

    search_fields = ['slug']
    list_editable=['slug','file','button_text',]

    class Meta:
        model = Document


    




        