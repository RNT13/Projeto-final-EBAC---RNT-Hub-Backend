from django.core.files.storage import default_storage
from rest_framework import serializers

from users.serializers.publicSerializer import UserPublicSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)
    image = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "content",
            "image",
            "created_at",
            "likes_count",
            "comments_count",
        ]
        read_only_fields = [
            "id",
            "author",
            "created_at",
            "likes_count",
            "comments_count",
        ]

    def get_image(self, obj):
        if obj.image:
            return default_storage.url(obj.image.path)
        return None
