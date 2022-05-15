from django.urls import path
from .views import dashboard
from .views import dashboard, profile_list, profile


urlpatterns = [
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("", dashboard, name="dashboard"),
]
