from django.conf.urls import url
from django.urls import path
from django.urls import include
from . import views


app_name = 'walls'


urlpatterns = [
    path('', views.wall, name="home_path"),
    path('administrator/', views.administrator_wall, name="administrator_path"),
]