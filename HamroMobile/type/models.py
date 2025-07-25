from django.db import models
from django.utils.text import slugify

class Type(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Type, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
