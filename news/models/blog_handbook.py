from django.utils.text import slugify

from shared.django import SlugBaseModel


class Category(SlugBaseModel):
    pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)


class Region(SlugBaseModel):
    pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Region.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)
