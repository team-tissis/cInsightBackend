from rest_framework import serializers 
from api.models import Proposal
 
 
class ProposalSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Proposal
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")