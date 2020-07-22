from django.contrib import admin
from .models import Section, Category, Packages, Bookings, Blogs

# Register your models here.

admin.site.register([Section, Category, Packages, Bookings, Blogs])
