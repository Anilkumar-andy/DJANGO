from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='_home'),
    path('contact/', views.contact,name='_contact'),
    path('about/', views.about,name='_about'),
]