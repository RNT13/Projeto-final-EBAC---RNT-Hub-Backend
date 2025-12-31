from django.urls import path

from comments.views.commentDetailView import CommentDetailView
from comments.views.commentListCreateView import CommentListCreateView

urlpatterns = [
    # /api/v1/posts/<post_id>/comments/
    path(
        "posts/<int:post_id>/comments/",
        CommentListCreateView.as_view(),
        name="post-comments",
    ),
    # /api/v1/posts/<post_id>/comments/<id>/
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        CommentDetailView.as_view(),
        name="comment-detail",
    ),
]
