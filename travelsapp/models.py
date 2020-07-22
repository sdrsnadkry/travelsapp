from django.db import models
from PIL import Image
from django_resized import ResizedImageField
from tinymce.models import HTMLField

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Section(TimeStamp):
    section_name = models.CharField(max_length=200)
    section_url = models.CharField(max_length=1024)
    section_desc = models.CharField(max_length=1024)

    def __str__(self):
        return self.section_name


class Category(TimeStamp):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    # section_name = models.CharField(max_length=100, default="")
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    category_name = models.CharField(max_length=100, default="")
    category_url = models.CharField(max_length=100, default="")
    category_desc = models.TextField(default="")
    popular = models.BooleanField(default=True)
    meta_tags = models.CharField(max_length=1024, default="")
    meta_keywords = models.CharField(max_length=2048, default="")
    meta_description = models.CharField(max_length=5000, default="")
    category_image = models.ImageField(
        upload_to="BackendImages/Category", default="")

    def __str__(self):
        return self.category_name


class Packages(TimeStamp):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    package_name = models.CharField(max_length=100, default="")
    package_url = models.CharField(max_length=100, default="")
    package_price = models.IntegerField()
    package_discount = models.IntegerField()
    package_overview = models.TextField( default="")
    package_itinerary = models.TextField(default="")
    meta_tags = models.CharField(max_length=1024, default="")
    meta_keywords = models.CharField(max_length=2048, default="")
    meta_description = models.CharField(max_length=100000, default="")
    package_image =ResizedImageField(size=[1920, 1080], quality=100, upload_to='BackendImages/Packages')
    best_value = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)


class Bookings(TimeStamp):
    package_name = models.CharField(max_length=100, default="")
    fullname = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=50, default="")
    count = models.CharField(max_length=100, default="")
    date = models.DateField()
    pickup = models.CharField(max_length=2000, default="")
    message = models.CharField(max_length=1000, default="")


class Blogs(TimeStamp):
    title = models.CharField(max_length=500, default="")
    author = models.CharField(max_length=500, default="")
    Date = models.DateField()
    content = models.TextField(default="")
    image = ResizedImageField(size=[1920, 1080], quality=100, upload_to='BackendImages/Blogs')
    



    
