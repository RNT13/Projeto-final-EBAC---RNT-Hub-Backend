# -------------------------------------------------------------------
# URLs do app de Comments (Comentários)
# -------------------------------------------------------------------
# Este módulo agrupa todas as rotas relacionadas aos comentários:
# - CRUD de comentários
# - Comentários por post específico
# - Rotas automáticas via DRF Router
# -------------------------------------------------------------------

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostCommentsView

# -------------------------------------------------------------------
# DRF Router - gera rotas REST automaticamente
# /api/v1/comments/
# /api/v1/comments/<id>/
# -------------------------------------------------------------------
router = DefaultRouter()
router.register("", CommentViewSet, basename="comments")

# -------------------------------------------------------------------
# Rotas manuais adicionais
# -------------------------------------------------------------------
urlpatterns = [
    # Lista comentários de um post específico
    # GET /api/v1/comments/post/<post_id>/
    path(
        "post/<int:post_id>/",
        PostCommentsView.as_view(),
        name="comments-by-post",
    ),
]

# Adiciona as rotas automáticas do router
urlpatterns += router.urls
