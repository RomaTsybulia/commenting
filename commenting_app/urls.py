from django.urls import path, include
from rest_framework import routers

from commenting_app.views import CommentViewSet

router = routers.DefaultRouter()
router.register("comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path(
        "comments/<int:pk>/add_reply/",
        CommentViewSet.as_view({"post": "add_reply"}),
        name="reply-add"
    ),
]

app_name = 'commenting_app'
