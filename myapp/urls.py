from django.urls import path
from . import views 
from django.conf import settings

urlpatterns=[
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user/userhomepage', views.userhomepage, name='userhomepage'),
    path('user/about', views.about, name='about'),
    path('user/contact', views.contact, name='contact'),
    path("logout/", views.logout, name="logout"),
    path("OTPVerification/", views.OTPVerification, name="OTPVerification"),
    path("adminhomepage/", views.adminhomepage, name="adminhomepage"),
    path('user/gaming', views.gaming, name='gaming'),

     
]