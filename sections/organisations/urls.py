from django.urls import path
from . import views
from django.urls import path, include

app_name = 'organisations'

urlpatterns = [
    path('create/', views.create, name="create_path"),
    path('join-reqs/', views.index_joinreqs, name="index_joinreqs_path"),
    path('join-reqs/a/<int:id>/', views.accept_joinreq, name="accept_joinreq_path"),
    path('join-reqs/d/<int:id>/', views.accept_joinreq, name="decline_joinreq_path"),
    path('<int:id_o>/home/', views.home, name="home_path"),
    path('<int:id_o>/home/a/<int:id_j>/', views.accept_user_joinreq, name="accept_user_joinreq_path"),
    path('<int:id_o>/home/d/<int:id_j>/', views.decline_user_joinreq, name="decline_user_joinreq_path"),
    path('join/', views.joinreq, name="joinreq_path"),
]
