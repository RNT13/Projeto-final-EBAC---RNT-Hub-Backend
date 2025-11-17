from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "author_username",
            "content",
            "image",
            "created_at",
            "updated_at",
            "likes_count",
            "comments_count",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "likes_count", "comments_count"]
        extra_kwargs = {"author": {"read_only": True}}


class PostCommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author",
            "author_username",
            "content",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "author"]
