from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, status, mixins
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CommentSerializer, GroupSerializer,
                             PostSerializer, FollowSerializer)
from posts.models import Comment, Group, Post, Follow

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]

    def get_post(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(post=post, author=self.request.user)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        follow_user_username = self.request.data.get('following')
        follow_user = User.objects.get(username=follow_user_username)
        if Follow.objects.filter(user=self.request.user,
                                 following=follow_user).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance = serializer.save(user=self.request.user,
                                   following=follow_user)
        # Возвращаем ответ с данными созданной подписки, используя сериализатор
        return Response(FollowSerializer(instance).data,
                        status=status.HTTP_201_CREATED)
