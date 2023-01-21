from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from news.models import Blog


@registry.register_document
class BlogDocument(Document):
    class Index:
        name = 'Blogs'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Blog
        fields = [
            'id',
            'name',
            'description'
        ]
