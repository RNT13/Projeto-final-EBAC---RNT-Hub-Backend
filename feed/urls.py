# -------------------------------------------------------------------
# Este módulo define todas as rotas envolvendo feeds:
# - Feed do usuário
# - Feed global / explore
# - Feed apenas com imagens
# - Feed por algoritmo (likes + comentários)
# -------------------------------------------------------------------

from rest_framework.routers import DefaultRouter

from .views import FeedViewSet

# -------------------------------------------------------------------
# DRF Router — rotas automáticas para actions do FeedViewSet
# /api/v1/feed/user/
# /api/v1/feed/explore/
# /api/v1/feed/images/
# /api/v1/feed/algorithm/
# -------------------------------------------------------------------
router = DefaultRouter()
router.register("", FeedViewSet, basename="feed")

# -------------------------------------------------------------------
# Rotas personalizadas (se houver futuras)
# -------------------------------------------------------------------
urlpatterns = router.urls
