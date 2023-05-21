from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me/", views.Me.as_view()),
    path("log-out/", views.LogOut.as_view()),
    path("github", views.GithubLogIn.as_view()),
    path("kakao", views.KakaoLogIn.as_view()),
    path("google", views.GoogleLogIn.as_view()),
    path("naver", views.NaverLogIn.as_view()),
]
