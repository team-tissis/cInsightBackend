from rest_framework import serializers 
from api.models import Lecture
from api.serializers.comment_serializer import CommentSerializer
 
 
class PureLectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
 
 
class DetailLectureSerializer(PureLectureSerializer):
    comments = CommentSerializer(many=True, read_only=True)