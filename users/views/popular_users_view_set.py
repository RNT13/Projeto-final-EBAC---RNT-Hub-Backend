from django.db.models import Count, F
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.models import User
from users.serializers.user_serializer import UserSerializer


class PopularUsersViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return (
            User.objects.annotate(
                followers_count=Count("followers", distinct=True),
                posts_count=Count("posts", distinct=True),
                likes_count=Count("posts__likes", distinct=True),
                comments_count=Count("posts__comments", distinct=True),
            )
            .annotate(
                popularity_score=F("followers_count") * 3
                + F("likes_count") * 2
                + F("comments_count") * 3
                + F("posts_count")
            )
            .filter(popularity_score__gt=0)
            .order_by("-popularity_score", "-followers_count")
        )
