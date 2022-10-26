from typing import List

from django.db import models
from django.db.models import When, Case
from django_filters import rest_framework as filters
from django_filters.constants import EMPTY_VALUES
from rest_framework import pagination



class NoPagination(pagination.PageNumberPagination):
    page_size = 100000


class CustomPagination(pagination.PageNumberPagination):
    page_size = 100000
    page_size_query_param = "per_page"


class InFilter(filters.CharFilter):
    def __init__(self, *args, **kwargs):
        super(InFilter, self).__init__(*args, **kwargs)
        self.method = 'selection_order'

class CharInFilter(filters.CharFilter):
    def __init__(self, *args, **kwargs):
        super(CharInFilter, self).__init__(*args, **kwargs)
        self.method = 'in_filter'


class BaseFilterSet(filters.FilterSet):
    def selection_order(self, queryset, value, *args, **kwargs):
        try:
            if args:
                values = args[0].split(',')
                preserved = Case(*[When(**{value: val, "then": pos}) for pos, val in enumerate(values)])
                queryset = queryset.filter(**{value+"__in": values}).order_by(preserved)
        except ValueError:
            queryset = None
            pass
        return queryset
    
    def in_filter(self, queryset, value, *args, **kwargs):
        try:
            if args:
                values = args[0].split(',')
                queryset = queryset.filter(**{value+"__in": values})
        except ValueError:
            queryset = None
            pass
        return queryset
 

class EmptyStringFilter(filters.BooleanFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        exclude = self.exclude ^ (value is False)
        if self.distinct:
            qs = qs.distinct()
        method = qs.exclude if exclude else qs.filter
        return method(**{self.field_name: ""})


def create_order_choices(instance: models.Model, model_name: str) -> List[tuple[str, str]]:
    attrs = [item for item in vars(instance).items()]
    choices: List[tuple[str, str]] = []
    for attr in attrs:
        name: str = "{}_{}".format(model_name, attr[0])
        choices.append((name, "{} {}".format(name, "asc")))
        choices.append(("-" + name, "{} {}".format(name, "desc")))
    return choices


def create_all_order_choices() -> List[tuple[str, str]]:
    tables: dict[str, models.Model] = {}
    choices: List[tuple[str, str]] = []
    for model_name, instance in tables.items():
        choices.extend(create_order_choices(instance, model_name))

    return choices


def create_order_fields(instance: models.Model, model_name: str, access_prefix: str) -> dict[str, str]:
    attrs = [item for item in vars(instance).items()]
    fields: dict[str, str] = {}
    for attr in attrs:
        param_name: str = "{}_{}".format(model_name, attr[0])
        field_name: str = "{}{}".format(access_prefix, attr[0])
        fields[field_name] = param_name
    return fields
