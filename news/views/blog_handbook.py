from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from news.models import Category, Region
from news.permissions import ReadOnly
from news.serializers.blog_handbook import CategoryModelSerializer, RegionModelSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    # permission_classes = [IsAdminUser | ReadOnly]
