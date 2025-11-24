from rest_framework import mixins, permissions, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserSerializer


# -------------------------------------------------------------------
# 1. Registro de usuário
# -------------------------------------------------------------------
class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


# -------------------------------------------------------------------
# 2. Perfil do usuário logado (GET e PATCH)
# -------------------------------------------------------------------
class UserMeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    # GET /me/
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # PATCH /me/
    def partial_update(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# -------------------------------------------------------------------
# 3. Listar todos os usuários (READ ONLY)
# -------------------------------------------------------------------
class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
