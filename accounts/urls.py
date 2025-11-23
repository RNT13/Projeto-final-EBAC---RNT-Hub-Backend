# -------------------------------------------------------------------
# URLs do app de Accounts (Usuários)
# -------------------------------------------------------------------
# Este módulo organiza todas as rotas relacionadas a usuários:
# - Registro (signup)
# - Perfil do usuário autenticado (me)
# - Listagem de usuários
# - Endpoints via ViewSets (DRF Router)
# -------------------------------------------------------------------

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AccountViewSet,
    UserMeViewSet,
    UserRegisterViewSet,
)

# -------------------------------------------------------------------
# DRF Router - rotas automáticas
# -------------------------------------------------------------------
router = DefaultRouter()

# /api/v1/accounts/me/
router.register("me", UserMeViewSet, basename="me")

# /api/v1/accounts/
router.register("", AccountViewSet, basename="accounts")

# -------------------------------------------------------------------
# Rotas manuais
# -------------------------------------------------------------------
urlpatterns = [
    # Registro de usuário
    # POST /api/v1/accounts/register/
    path(
        "register/",
        UserRegisterViewSet.as_view({"post": "create"}),
        name="register",
    ),
]

# Adiciona as rotas automáticas do router
urlpatterns += router.urls
