from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def get_queryset(self):
        pk_post = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=pk_post)
        return post.comments

    def perform_create(self, serializer):
        pk_post = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=pk_post)
        serializer.save(author=self.request.user, post=post)
