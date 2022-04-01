from django.urls import path, include
from django import urls
from store import views



app_name = 'store2'

urlpatterns = [
    path('CategoryDelete',views.CategoryDelete, name='CategoryDelete'),
    path('category', views.Category_Out_All_Data, name='category'),
    path('Updata/<int:id>/', views.CategoryUpdata, name='Updata'),
    path('NewCategory2', views.NewCategory2Func, name='NewCategory'),
    path('ItemAddPath', views.ItemAdd, name='ItemAdd'),
    path('ItemDataPath', views.ItemDataAllOut, name='ItemDataPath'),
    path('BootstrapTestPath', views.BootstrapTestFunc, name='BootstrapTestPath'),

]
