from django.urls import path
from bloghome import views

urlpatterns = [
    path('/myDiary',views.home),
    path('/search',views.mydiaryserch),
    path('/about',views.mydiaryabout),
    path('/contact',views.mydiarycontact),
]
