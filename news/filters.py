from django_filters import FilterSet, CharFilter

from news.models import Blog


class BlogFilter(FilterSet):
    tag = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ('category', 'region__name', 'tag')
