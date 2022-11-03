from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filters import CustomPagination, NoPagination
from api.models import Proposal
from api.serializers.proposal_serializer import ProposalSerializer


class ProposalFilter(filters.FilterSet):
    class Meta:
        model = Proposal
        fields = "__all__"


class ProposalViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Proposal] = Proposal.objects.all()
    serializer_class = ProposalSerializer
    filter_class = ProposalFilter
    pagination_class = CustomPagination
