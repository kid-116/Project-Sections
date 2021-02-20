from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage_path"),
    path('accounts/', include('accounts.urls')),
    path('orgs/', include('organisations.urls')),
    path('wall/', include('walls.urls')),
    path('orgs/brackets/', include('brackets.urls')),
]


urlpatterns += staticfiles_urlpatterns()
