from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AccountViewSet,
    UserMeViewSet,
    UserRegisterViewSet,
)

router = DefaultRouter()

# /api/v1/accounts/me/
router.register("me", UserMeViewSet, basename="me")

# /api/v1/accounts/
router.register("", AccountViewSet, basename="accounts")

urlpatterns = [
    # POST /api/v1/accounts/register/
    path(
        "register/",
        UserRegisterViewSet.as_view({"post": "create"}),
        name="register",
    ),
]

urlpatterns += router.urls
