from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from .models import Follow
from .serializers import FollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Lista apenas PESSOAS que o usuário autenticado segue
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer):
        follower = self.request.user
        following = serializer.validated_data["following"]

        # 1. Não pode seguir a si mesmo
        if follower == following:
            raise ValidationError("Você não pode seguir a si mesmo.")

        # 2. Não pode seguir duas vezes
        if Follow.objects.filter(follower=follower, following=following).exists():
            raise ValidationError("Você já está seguindo esse usuário.")

        serializer.save(follower=follower)
