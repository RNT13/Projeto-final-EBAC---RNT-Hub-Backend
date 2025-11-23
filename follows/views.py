from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import ValidationError

from .models import Follow
from .serializers import FollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de Follows:
    - list: quem o usuário autenticado segue
    - create: seguir outro usuário
    """

    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Lista apenas pessoas que o usuário autenticado segue
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer):
        follower = self.request.user
        following = serializer.validated_data["following"]

        if follower == following:
            raise ValidationError("Você não pode seguir a si mesmo.")

        if Follow.objects.filter(follower=follower, following=following).exists():
            raise ValidationError("Você já está seguindo esse usuário.")

        serializer.save(follower=follower)


class FollowersListView(generics.ListAPIView):
    """
    Lista todos os seguidores de um usuário específico
    """

    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Follow.objects.filter(following_id=user_id)


class FollowingListView(generics.ListAPIView):
    """
    Lista todos os usuários que um usuário específico está seguindo
    """

    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Follow.objects.filter(follower_id=user_id)
