# Generated by Django 5.0.6 on 2024-05-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_remove_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
