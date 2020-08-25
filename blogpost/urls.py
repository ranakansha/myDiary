from django.urls import path
from blogpost import views

urlpatterns = [
    path('/post',views.home),
    # api for post cooment
    path('/postcomment',views.postcomment,name="postcomment"),

    path('/savepost/<str:slug>',views.savepost),
    path('/viewpost/<str:slug>',views.viewpost),
    path('/deletepost/<str:slug>',views.deletepost),
    ]