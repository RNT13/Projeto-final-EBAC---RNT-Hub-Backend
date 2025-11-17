from rest_framework import status
from rest_framework.test import APITestCase

from .factories import FollowFactory, UserFactory


class FollowAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.other_user = UserFactory()

    def test_follow_user(self):
        response = self.client.post("/api/v1/follows/", {"following": self.other_user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["follower"], self.user.id)

    def test_list_follows(self):
        FollowFactory(follower=self.user, following=self.other_user)
        response = self.client.get("/api/v1/follows/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
