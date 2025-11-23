# -------------------------------------------------------------------
# URLs do app de Follows (Seguidores)
# -------------------------------------------------------------------
# Este módulo contém todas as rotas relacionadas ao sistema de seguir:
# - Seguir / deixar de seguir
# - Listar quem o usuário segue
# - Listar seguidores de um usuário
# - Rotas automáticas via DRF Router
# -------------------------------------------------------------------

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FollowersListView, FollowingListView, FollowViewSet

# -------------------------------------------------------------------
# DRF Router - CRUD básico:
# /api/v1/follows/
# /api/v1/follows/<id>/
# -------------------------------------------------------------------
router = DefaultRouter()
router.register("", FollowViewSet, basename="follows")

# -------------------------------------------------------------------
# Rotas personalizadas
# -------------------------------------------------------------------
urlpatterns = [
    # Lista quem segue o usuário X
    # GET /api/v1/follows/<user_id>/followers/
    path(
        "<int:user_id>/followers/",
        FollowersListView.as_view(),
        name="followers-list",
    ),
    # Lista quem o usuário X está seguindo
    # GET /api/v1/follows/<user_id>/following/
    path(
        "<int:user_id>/following/",
        FollowingListView.as_view(),
        name="following-list",
    ),
]

# Adiciona rotas automáticas do router
urlpatterns += router.urls
