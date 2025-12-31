from django.urls import path

from likes.views.likeToggleView import LikeToggleView
from likes.views.postLikesListView import PostLikesListView

urlpatterns = [
    # Curtir / descurtir
    # POST /api/v1/likes/posts/<post_id>/
    path(
        "posts/<int:post_id>/",
        LikeToggleView.as_view(),
        name="like-toggle",
    ),
    # Listar usuários que curtiram
    # GET /api/v1/likes/posts/<post_id>/users/
    path(
        "posts/<int:post_id>/users/",
        PostLikesListView.as_view(),
        name="post-likes-list",
    ),
]
