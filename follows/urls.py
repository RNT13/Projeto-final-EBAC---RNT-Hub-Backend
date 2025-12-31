from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FollowersListView, FollowingListView

router = DefaultRouter()

urlpatterns = [
    # GET /api/v1/follows/<user_id>/followers/
    path(
        "<int:user_id>/followers/",
        FollowersListView.as_view(),
        name="followers-list",
    ),
    # GET /api/v1/follows/<user_id>/following/
    path(
        "<int:user_id>/following/",
        FollowingListView.as_view(),
        name="following-list",
    ),
]

urlpatterns += router.urls
