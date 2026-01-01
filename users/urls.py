from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views.popular_users_view_set import PopularUsersViewSet
from users.views.user_view_set import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path(
        "popular/",
        PopularUsersViewSet.as_view({"get": "list"}),
        name="popular-users",
    ),
]

urlpatterns += router.urls
