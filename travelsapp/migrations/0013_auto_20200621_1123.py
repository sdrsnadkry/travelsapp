# Generated by Django 3.0.7 on 2020-06-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0012_category_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='', upload_to='BackendImages/Category'),
        ),
    ]
