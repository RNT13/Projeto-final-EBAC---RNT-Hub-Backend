from rest_framework import status
from rest_framework.test import APITestCase

from .factories import LikeFactory, PostFactory, UserFactory


class LikeAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.post = PostFactory(author=self.user)

    def test_like_post(self):
        response = self.client.post("/api/v1/likes/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], self.user.id)

    def test_list_likes(self):
        LikeFactory(user=self.user, post=self.post)
        response = self.client.get("/api/v1/likes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
