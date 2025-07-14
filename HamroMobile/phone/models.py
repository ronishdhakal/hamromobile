from django.db import models
from django.utils.text import slugify
from brand.models import Brand
from category.models import Category
from segment.models import Segment
from type.models import Type


class Phone(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)

    priority = models.IntegerField(null=True, blank=True)

    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    display_title = models.CharField(max_length=100, default="Display")
    display_value = models.CharField(max_length=255, blank=True, null=True)

    camera_title = models.CharField(max_length=100, default="Camera")
    camera_value = models.CharField(max_length=255, blank=True, null=True)

    processor_title = models.CharField(max_length=100, default="Processor")
    processor_value = models.CharField(max_length=255, blank=True, null=True)

    battery_title = models.CharField(max_length=100, default="Battery")
    battery_value = models.CharField(max_length=255, blank=True, null=True)

    memory_title = models.CharField(max_length=100, default="Memory")
    memory_value = models.CharField(max_length=255, blank=True, null=True)

    fiveg_title = models.CharField(max_length=100, default="5G")
    has_5g = models.BooleanField(default=False)

    buy_link = models.URLField(max_length=500, blank=True, null=True)  # <-- added buy link

    types = models.ManyToManyField(Type, related_name='phones', blank=True)

    features_image = models.ImageField(upload_to='phone/features/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PriceVariant(models.Model):
    phone = models.ForeignKey(Phone, related_name='price_variants', on_delete=models.CASCADE)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    price_npr = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ram} + {self.storage} - {self.price_npr} NPR"

    class Meta:
        verbose_name_plural = "Price Variants"


class GalleryImage(models.Model):
    phone = models.ForeignKey(Phone, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phone/gallery/')

    def __str__(self):
        return f"Gallery for {self.phone.name}"

    class Meta:
        verbose_name_plural = "Gallery Images"


class CameraSample(models.Model):
    phone = models.ForeignKey(Phone, related_name='camera_samples', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phone/camera_samples/')

    def __str__(self):
        return f"Camera sample for {self.phone.name}"

    class Meta:
        verbose_name_plural = "Camera Samples"


class PhoneSpecSection(models.Model):
    phone = models.ForeignKey(Phone, related_name='spec_sections', on_delete=models.CASCADE)
    section_name = models.CharField(max_length=100, default='General')

    def __str__(self):
        return f"{self.phone.name} - {self.section_name}"

    class Meta:
        verbose_name_plural = "Phone Spec Sections"


class PhoneSpecTitle(models.Model):
    section = models.ForeignKey(PhoneSpecSection, related_name='titles', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.section.section_name} - {self.title}"

    class Meta:
        verbose_name_plural = "Titles"


class PhoneSpecValue(models.Model):
    title = models.ForeignKey(PhoneSpecTitle, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title.title}: {self.value}"

    class Meta:
        verbose_name_plural = "Values"
