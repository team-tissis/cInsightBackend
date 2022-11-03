from django.db.models import QuerySet
from django_filters import rest_framework as filters

from api.filters import CustomPagination, NoPagination
from api.models import Proposal
from api.serializers.proposal_serializer import ProposalSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status


class ProposalFilter(filters.FilterSet):
    class Meta:
        model = Proposal
        fields = "__all__"


class ProposalViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Proposal] = Proposal.objects.all()
    serializer_class = ProposalSerializer
    filter_class = ProposalFilter
    pagination_class = CustomPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProposalSerializer(instance)
        return Response({"proposal": serializer.data}, status=status.HTTP_200_OK)