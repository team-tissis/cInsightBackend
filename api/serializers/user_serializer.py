from rest_framework import serializers 
from api.models import CustomeUser
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")