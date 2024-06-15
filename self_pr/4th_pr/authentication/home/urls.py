from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="_home" ),
    path('ListAc',views.account_list,name="account_list")
]
