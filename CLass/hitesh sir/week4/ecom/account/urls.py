from django.urls import path
from . import views

urlpatterns = [
   path("login/", views.Login_View.as_view(),name="-login"),
   path("register/", views.register,name="-register"),
   path('logout/',views.logout_user,name="-logout")
]
