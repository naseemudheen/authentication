from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('login', LoginPageView.as_view(), name="login"),
    path('', HomePageView.as_view(), name="index"),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'user/login.html'),name ="logout"),
    path('getdata', getdata, name="getdata"),
]