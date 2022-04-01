from LearnForAllauth import urls
from django.urls import path, include
from MainPage import views

urlpatterns = [
    path('News', views.News, name='News'),
    path('Center', views.Center, name='Center'),
]
