from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('login', LoginPageView.as_view(), name="login"),
    path('', HomePageView.as_view(), name="index"),
    path('logout/',LogoutPageView.as_view(),name ="logout"),
    path('register/',RegisterPageView.as_view(), name ="register"),

    # path('getdata', getdata, name="getdata"),
]