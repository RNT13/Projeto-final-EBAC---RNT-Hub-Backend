# -------------------------------------------------------------------
# URLs do app de Likes
# -------------------------------------------------------------------
# Este módulo define todas as rotas envolvendo curtidas:
# - Curtir um post
# - Remover curtida
# - Listar likes de um post
# -------------------------------------------------------------------

from rest_framework.routers import DefaultRouter

from .views import LikeViewSet

# -------------------------------------------------------------------
# DRF Router — rotas automáticas:
# /api/v1/likes/
# /api/v1/likes/<id>/
# -------------------------------------------------------------------
router = DefaultRouter()
router.register("", LikeViewSet, basename="likes")

# -------------------------------------------------------------------
# Rotas personalizadas
# -------------------------------------------------------------------
urlpatterns = router.urls
