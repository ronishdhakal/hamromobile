from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from brand.models import Brand
from category.models import Category
from segment.models import Segment

class Review(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.ImageField(upload_to='reviews/featured/')
    featured = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='reviews')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='reviews')
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='reviews')
    summary = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ReviewSection(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=255)  # e.g., "Design & Build"
    rating = models.DecimalField(max_digits=4, decimal_places=1)  # scale of 10
    text = RichTextUploadingField()  # <-- updated for CKEditor

    def __str__(self):
        return f"{self.review.title} - {self.name}"


class ReviewSectionGallery(models.Model):
    section = models.ForeignKey(ReviewSection, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='reviews/sections/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.section.name} Image"
