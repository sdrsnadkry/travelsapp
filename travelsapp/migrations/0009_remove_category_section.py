# Generated by Django 3.0.7 on 2020-06-16 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0008_remove_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='section',
        ),
    ]