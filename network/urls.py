
from django.urls import path

from . import views

urlpatterns = [



    path("", views.index, name="index"),
    path("post", views.post, name="post"),
    path("profile/<str:u_name>", views.profile, name="profile"),
    path("following", views.following, name="following"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # api
    path("like/<str:p_id>", views.like, name="like"),
    path("edit/<str:p_id>", views.edit, name="edit"),
]
