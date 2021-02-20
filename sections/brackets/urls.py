from django.conf.urls import url
from django.urls import path
from brackets import views


app_name = 'brackets'


urlpatterns = [
    path('create/at/<int:id_o>/', views.create, name="create_path"),
    path('<int:id_b>/home/', views.home, name="home_path"),
    path('create_joinreq/at/<int:id_b>/', views.create_joinreq, name="create_joinreq_path"),
    path('<int:id_o>/index/', views.index, name="index_path"),
    path('areq/<int:id_r>/', views.accept_joinreq, name="accept_joinreq_path"),
    path('dreq/<int:id_r>/', views.decline_joinreq, name="decline_joinreq_path"),
]