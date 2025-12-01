from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # ---------------------------------------------------------
    # 📘 Documentação da API
    # ---------------------------------------------------------
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # ---------------------------------------------------------
    # Admin
    # ---------------------------------------------------------
    path("admin/", admin.site.urls),
    # ---------------------------------------------------------
    # JWT Authentication
    # ---------------------------------------------------------
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # ---------------------------------------------------------
    # Apps da API
    # ---------------------------------------------------------
    path("api/v1/users/", include("users.urls")),
    path("api/v1/posts/", include("posts.urls")),
    path("api/v1/likes/", include("likes.urls")),
    path("api/v1/follows/", include("follows.urls")),
    path("api/v1/notifications/", include("notifications.urls")),
    path("api/v1/feed/", include("feed.urls")),
]

# ✅ SERVIR MEDIA EM DESENVOLVIMENTO
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
