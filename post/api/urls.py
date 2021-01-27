from django.urls import include, path
from rest_framework import routers
from post.api import views
from ..models import Like


urlpatterns = [
    path('likes/',views.LikeListView.as_view())
]