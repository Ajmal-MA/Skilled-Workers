from django.urls import path
from . import views

urlpatterns = [
    path("auth/", views.login_page, name="login_page"),
    path("logout/", views.logout_view, name="logout"),
]
