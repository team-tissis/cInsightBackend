from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filters import NoPagination
from api.models import Comment
from api.serializers.comment_serializer import CommentSerializer


class CommentFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Comment] = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_class = CommentFilter
    pagination_class = NoPagination
