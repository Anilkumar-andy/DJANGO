from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='_index'),
    path('carlist',views.carlist , name='_carlist'),
    path('update/<id>/', views.update , name='_update'),
    path('delete/<id>/', views.delete , name='_delete'),
]
