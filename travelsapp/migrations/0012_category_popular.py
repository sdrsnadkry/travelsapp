# Generated by Django 3.0.7 on 2020-06-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0011_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='popular',
            field=models.BooleanField(default=True),
        ),
    ]