from django.conf.urls import url
from django.urls import path
from brackets import views


app_name = 'brackets'


urlpatterns = [
    path('create/at/<int:id_o>', views.create, name="create_path"),
    # url('index-joinreqs/', views.index_joinreqs, name="index_joinreqs_path"),
    # url('index/', views.index, name="index_brackets_path"),
    # url('join/', views.join, name="join_bracket_path"),
    # path('areq/<int:id>/', views.accept_join_req, name="accept_req_path"),
    # path('dreq/<int:id>/', views.decline_join_req, name="decline_req_path"),
]