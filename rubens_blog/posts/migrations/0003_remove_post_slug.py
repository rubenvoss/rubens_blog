# Generated by Django 5.0.6 on 2024-05-24 09:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_post_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
    ]
