from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from api.models import CustomeUser
from api.filters import NoPagination
from api.serializers.user_serializer import UserSerializer
from rest_framework.response import Response


class UserFilter(filters.FilterSet):
    class Meta:
        model = CustomeUser
        fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[CustomeUser] = CustomeUser.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    pagination_class = NoPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)