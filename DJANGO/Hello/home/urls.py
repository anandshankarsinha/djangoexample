from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='HOME'),
    path('about', views.about, name='ABOUT'),

    path('services', views.services, name='SERVICES'),
    path('contact', views.contact, name='CONTACT')
]

