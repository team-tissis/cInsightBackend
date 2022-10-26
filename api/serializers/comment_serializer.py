from rest_framework import serializers 
from api.models import Comment
 
 
class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "code", "created_at", "updated_at")