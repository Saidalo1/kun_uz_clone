from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
import os

from news.filters import BlogFilter
from news.models import Blog
from news.permissions import ReadOnly
from news.serializers.blog import BlogModelSerializer
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
