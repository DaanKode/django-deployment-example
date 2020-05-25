from django.conf.urls import url
from fifth_app import views
from django.urls import path

app_name = "fifth_app"

urlpatterns = [
    path("register/", views.registration, name="registration"),
    path("user_login", views.user_login, name="user_login"),
]
