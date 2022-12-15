from rest_framework.serializers import ModelSerializer

from news.models import Category, Region


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug',)


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('slug',)
