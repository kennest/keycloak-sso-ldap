from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_from_app_1, name="hello"),
    path("logout/", views.logout_view, name="logout"),
]
