from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("profile/", profile, name="profile"),
    path('', include('social_django.urls', namespace='social')),
]