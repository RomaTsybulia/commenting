from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, \
    permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from commenting_app.models import Comment
from commenting_app.serializers import CommentSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CommentViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all().select_related("author")
        if self.action == "list":
            queryset = queryset.filter(head_comment=True)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Succes"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        if self.action == "create":
            serializer.validated_data["head_comment"] = True
        serializer.save(author=self.request.user)

    def add_reply(self, request, pk=None):
        main_comment = get_object_or_404(Comment, pk=pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reply = serializer.save(author=request.user)

        reply.main_comment = main_comment
        reply.save()
        return Response({"message": "Succes"}, status=status.HTTP_201_CREATED)
