import factory

from accounts.factories import UserFactory
from likes.models import Like
from posts.factories import PostFactory


class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
