from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from comments.serializers import CommentSerializer

from .models import Post
from .serializers import PostSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["get", "post"])
    def comments(self, request, pk=None):
        post = self.get_object()

        if request.method == "POST":
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # Evita comentários duplicados
            if post.comments_comments.filter(user=request.user, text=serializer.validated_data["text"]).exists():
                raise ValidationError({"detail": "Você já comentou isso neste post."})

            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        comments = post.comments_comments.all().order_by("created_at")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class UserPostsView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]

        # se o usuário não existir → erro 404
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({"detail": "Usuário não encontrado."})

        return Post.objects.filter(author=user).order_by("-created_at")
