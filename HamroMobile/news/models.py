from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from brand.models import Brand
from category.models import Category
from segment.models import Segment

class News(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='news')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='news')
    content = RichTextUploadingField()
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:500]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
