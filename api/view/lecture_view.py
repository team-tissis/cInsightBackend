from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets, status

from api.filters import CustomPagination, NoPagination
from api.models import Lecture
from api.serializers.lecture_serializer import PureLectureSerializer, DetailLectureSerializer

from rest_framework.response import Response

class LectureFilter(filters.FilterSet):
    class Meta:
        model = Lecture
        fields = "__all__"
        exclude = ["attendee_eoas"]


class LectureViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Lecture] = Lecture.objects.all()
    serializer_class = PureLectureSerializer
    filter_class = LectureFilter
    pagination_class = CustomPagination
    
    def retrieve(self, request, *args, **kwargs):
        print("hoge")
        instance = self.get_object()
        serializer = DetailLectureSerializer(instance)
        return Response({"lecture": serializer.data}, status=status.HTTP_200_OK)