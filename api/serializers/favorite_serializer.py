from rest_framework import serializers 
from api.models import Comment, CustomeUser, Favorite
from api.serializers.user_serializer import UserSerializer
from api.serializers.comment_serializer import CommentSerializer
 
 
class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(required=False)
    comment = CommentSerializer(many=False, read_only=True)
    commenter_id = serializers.IntegerField(required=False)
 
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ("id", "is_synced","vote_weight", "created_at", "updated_at")
