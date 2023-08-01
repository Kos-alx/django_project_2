from django_filters import FilterSet, DateTimeFilter, CharFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    title_contains = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Найти',
    )

    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата позже',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = []
