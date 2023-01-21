from django.db.models import F
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.fields import HiddenField, CurrentUserDefault, IntegerField
from rest_framework.serializers import ModelSerializer

from news.documents.adverts import BlogDocument
from news.models import Blog
from news.serializers.blog_handbook import CategoryModelSerializer, RegionModelSerializer


class BlogModelSerializer(ModelSerializer):
    views = IntegerField(read_only=True)
    author = HiddenField(default=CurrentUserDefault())

    def to_representation(self, instance):
        Blog.objects.filter(id=instance.id).update(views=F('views') + 1)
        represent = super().to_representation(instance)
        represent['category'] = CategoryModelSerializer(instance.category).data
        represent['region'] = RegionModelSerializer(instance.region).data
        return represent

    class Meta:
        model = Blog
        exclude = ('slug', 'created_at', 'updated_at')


class BlogDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BlogDocument
        fields = ('id', 'name', 'description')
