from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='CsiHome'),
    path('blog/', views.blog, name='CsiHome'),
    path('contact', views.contact, name='CsiHome'),
    path('elements', views.elements, name='CsiHome'),
    path('speakers', views.speakers, name='CsiHome'),
    path('tickets', views.tickets, name='CsiHome'),
]
