import factory

from accounts.factories import UserFactory
from notifications.models import Notification


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    user = factory.SubFactory(UserFactory)
    text = factory.Faker("sentence")
    is_read = False
