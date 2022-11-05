from rest_framework import serializers 
from api.models import Comment, CustomeUser
from api.serializers.user_serializer import UserSerializer
 
 
class CommentSerializer(serializers.ModelSerializer):
    lecture_id = serializers.IntegerField(required=False)
    commenter = UserSerializer(many=False, read_only=True)
 
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "code", "created_at", "updated_at")