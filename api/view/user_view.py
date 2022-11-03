from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filters import NoPagination
from api.models import User
from api.serializers.user_serializer import UserSerializer


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[User] = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    pagination_class = NoPagination
