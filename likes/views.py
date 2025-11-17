from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Lista curtidas feitas pelo usuário logado
        return Like.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data["post"]

        # Impedir curtir duas vezes
        if Like.objects.filter(user=user, post=post).exists():
            raise ValidationError("Você já curtiu este post.")

        serializer.save(user=user)
