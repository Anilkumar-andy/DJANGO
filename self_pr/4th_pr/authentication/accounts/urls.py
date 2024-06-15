from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page, name="_login" ),
    path('register/',views.register_page, name="_register" ),
    path('logout/',views.logout_page,name="_logout_page")
]
