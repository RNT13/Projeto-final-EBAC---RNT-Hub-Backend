import factory

from accounts.factories import UserFactory
from comments.models import Comment
from posts.factories import PostFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    text = factory.Faker("sentence")
