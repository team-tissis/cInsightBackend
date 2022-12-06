from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets, status

from api.filters import CustomPagination, NoPagination
from api.models import Comment, CustomeUser, Favorite
from api.serializers.favorite_serializer import FavoriteSerializer

from rest_framework.decorators import action
from api.utils import HttpMethod
from django.db import transaction
from rest_framework.request import Request
from rest_framework.response import Response

class FavoriteFilter(filters.FilterSet):
    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Favorite] = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_class = FavoriteFilter
    pagination_class = CustomPagination

    @transaction.atomic
    def create(self, request: Request, *args, **kwargs):
        commentId = request.data.get("comment_id")
        userId = request.data.get("user_id")
        if not ((commentId is not None) and (userId is not None)):
            return Response({"user": None, "message": "アカウントアドレスが指定されていません"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomeUser.objects.get(id=userId)
        comment = Comment.objects.get(id=commentId)
        if not (Favorite.objects.filter(user=user, comment=comment) is None):
            return Response({"user": None, "message": "すでにいいねされています"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Favorite.objects.create(user=user, comment=comment)
            if comment.favo is None:
                comment.favo = 0
            comment.favo += 1
            comment.save()
            return Response({"message": "コメントにいいねしました"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Commentが見つかりませんでした"}, status=status.HTTP_404_NOT_FOUND)

    @transaction.atomic
    def destroy(self, request: Request, *args, **kwargs):
        favoriteId = request.data.get("id")
        favorite = Favorite.objects.get(id=favoriteId)
        if favorite is None:
            return Response({"user": None, "message": "いいねが存在しません"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            comment = favorite.comment
            comment.favo -= 1
            comment.save()
            favorite.delete()
            return Response({"message": "コメントを取り消しました。"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "いいねが見つかりませんでした"}, status=status.HTTP_404_NOT_FOUND)
