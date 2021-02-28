from django.conf.urls import url
from django.urls import path
from django.urls import include
from . import views
from organisations.models import Organisation


app_name = 'walls'


urlpatterns = [
    path('my-orgs', views.orgs_wall, name="orgs_path"),
]