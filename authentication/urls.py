from django.urls import path,include
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.userlogin),
    path('signup',views.usersignup),
    path('logout',views.userlogout),
    path('accounts/', include('django.contrib.auth.urls')),

    
    
]
