from django.urls import path
from . import views
from django.views.generic import TemplateView   # to render the form as view directly



urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',TemplateView.as_view(template_name = 'account/choice.html'),name='register'),
    path('register/<str:user_type>/', views.register_user, name='register_user'),
    # path('register/supplier',views.register_supplier,name='register-supplier'),`
    # path('register/customer',views.register_customer,name='register-customer'),
    # path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('mail/',TemplateView.as_view(template_name ='account/email.html'),name='get_email_form'),
    path('end_mail/',views.mail_send,name='mail_send_')
]