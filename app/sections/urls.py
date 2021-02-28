from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage_path"),
    path('', include('walls.urls')),
    path('accounts/', include('accounts.urls')),
    path('orgs/', include('organisations.urls')),
    path('orgs/brackets/', include('brackets.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
