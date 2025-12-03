from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Lista apenas likes do usuário logado
        return Like.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data["post"]

        # Se já existe, remove o like (toggle)
        existing_like = Like.objects.filter(user=user, post=post).first()
        if existing_like:
            existing_like.delete()
            return Response({"detail": "Like removido."}, status=status.HTTP_200_OK)

        serializer.save(user=user)
