from django.urls import path, include

from Main import views

app_name = 'MainPage'

urlpatterns = [
    path('MainPage',views.Main, name='MainPage'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('Login', views.Login, name='Login'),

]
