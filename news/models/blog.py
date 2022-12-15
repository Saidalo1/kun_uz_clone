from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.db.models import ForeignKey, CASCADE, CharField, IntegerField, ImageField
from django.utils.text import slugify

from news.models.blog_handbook import Region, Category
from shared.django import SlugBaseModel, TimeBaseModel
from users.models import User


class Blog(SlugBaseModel, TimeBaseModel):
    name = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)
    description = RichTextField()
    region = ForeignKey(Region, CASCADE)
    author = ForeignKey(User, CASCADE)
    tag = ArrayField(CharField(max_length=255))
    views = IntegerField(default=0)
    image = ImageField(upload_to='blog-images/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Blog.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + f'{Blog.objects.filter(slug=self.slug).count()}'
        super().save(*args, **kwargs)
