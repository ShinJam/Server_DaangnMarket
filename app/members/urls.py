from django.urls import path
from .views import *


app_name = "members"
urlpatterns = [
    # 테스트 클라이언드 사이드
    path("front/", entry_view, name="front"),
    path("front_signup/", signup_view, name="signup_front"),
    # API
    path("login/", FirebaseLogin.as_view(), name="login"),
    path("signup/", SignUp.as_view(), name="signup"),
]
