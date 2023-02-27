import os

from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from news.documents.adverts import BlogDocument
from news.filters import BlogFilter
from news.models import Blog
from news.permissions import ReadOnly
from news.serializers.blog import BlogModelSerializer, BlogDocumentSerializer
from root.settings import BASE_DIR


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAdminUser | ReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BlogFilter

    def destroy(self, request, *args, **kwargs):
        if Blog.objects.get(id=kwargs.get('pk')).image.url:
            image_url = Blog.objects.get(id=kwargs.get('pk')).image.url
            os.remove(BASE_DIR / image_url)
        return super().destroy(request, *args, **kwargs)


class BlogDocumentViewSet(DocumentViewSet):
    document = BlogDocument
    serializer_class = BlogDocumentSerializer
    filter_backends = [CompoundSearchFilterBackend]
    search_fields = ('name', 'description')

