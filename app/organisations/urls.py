from django.urls import path
from . import views
from django.urls import path, include

app_name = 'organisations'

urlpatterns = [
    path('register/', views.register, name="register_path"),
    path('reg-reqs/', views.index_regreqs, name="index_regreqs_path"),
    path('reg-reqs/<int:id_o>/a/', views.accept_regreq, name="accept_regreq_path"),
    path('reg-reqs/<int:id_o>/d/', views.decline_regreq, name="decline_regreq_path"),
    path('<int:id_o>/home/', views.home, name="home_path"),
    path('<int:id_o>/admin/', views.admin_page, name="admin_page_path"),
    path('<int:id_o>/join-req/<int:id_j>/a/', views.accept_joinreq, name="accept_joinreq_path"),
    path('<int:id_o>/join-req/<int:id_j>/d/', views.decline_joinreq, name="decline_joinreq_path"),
    path('join/', views.joinreq, name="joinreq_path"),
]
