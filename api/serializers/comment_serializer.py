from rest_framework import serializers 
from api.models import Comment
 
 
class CommentSerializer(serializers.ModelSerializer):
    lecture_id = serializers.IntegerField(required=False)
 
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "code", "created_at", "updated_at")