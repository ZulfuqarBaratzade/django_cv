from django.contrib import admin
from django.urls import path
from .views import index,about,elements,services,porfolio,contact,blog,single_blog,redirect_url

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('blog',blog,name='blog'),
    path('elements',elements,name='elements'),
    path('services',services,name='services'),
    path('contact',contact,name='contact'),
    path('porfolio',porfolio,name='portfolio'),
    path('single-blog',single_blog,name='single-blog'),
    path('<slug>/', redirect_url,name='redirect_url')

]
