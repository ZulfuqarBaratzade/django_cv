from django.shortcuts import render,redirect,get_object_or_404
from core.models import General_Settings, ImageSettings, Skill, Experience,Education,SocialMedia,Document
# Create your views here.
def layout(request):
    site_title = General_Settings.objects.get(name='site_title').parameter
    site_keywords = General_Settings.objects.get(name='site_keywords').parameter
    site_description = General_Settings.objects.get(name='site_description').parameter
    home_banner_name = General_Settings.objects.get(name='home_banner_name').parameter
    home_banner_title = General_Settings.objects.get(name='home_banner_title').parameter
    home_banner_description = General_Settings.objects.get(name= 'home_banner_description').parameter
    about_myself_welcome = General_Settings.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = General_Settings.objects.get(name='about_myself_footer').parameter
    profile_photo = ImageSettings.objects.get(name='profile_photo').file
    skills = Skill.objects.all().order_by('order')
    experience = Experience.objects.all()
    education = Education.objects.all()
    social_media = SocialMedia.objects.all()
    document = Document.objects.all()


    context = {
        'site_title': site_title,
        'site_keywords':site_keywords,
        'site_description': site_description,
        'home_banner_name':home_banner_name,
        'home_banner_title':home_banner_title,
        'home_banner_description':home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer':about_myself_footer,
        'profile_photo':profile_photo,
        'skills': skills,
        'experience':experience,
        'education':education,
        'social_media':social_media,
        'document':document,

    }
    return context
def index(request):
    return render(request,'index.html')


def redirect_url(request,slug):
    doc = get_object_or_404(Document,slug=slug)
    return redirect(doc.file.url)

def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def porfolio(request):
    return render(request,'portfolio.html')
def services(request):
    return render(request,'services.html')
def elements(request):
    return render(request,'elements.html')
def single_blog(request):
    return render(request, 'single-blog.html')