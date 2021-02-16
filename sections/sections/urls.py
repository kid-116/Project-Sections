from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage_path"),
    path('accounts/', include('accounts.urls')),
    path('orgs/', include('organisations.urls')),
    path('wall/', include('walls.urls')),
    path('brackets/', include('brackets.urls')),
]
