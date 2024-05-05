# Generated by Django 5.0 on 2024-05-05 16:53

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_create_homepage"),
        ("wagtailcore", "0093_uploadedfile"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_cta",
            field=models.CharField(
                blank=True,
                help_text="Text to display on Call to Action",
                max_length=255,
                verbose_name="Hero CTA",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_cta_link",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose a page to link to for the Call to Action",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Hero CTA link",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_text",
            field=models.CharField(
                blank=True,
                help_text="Write an introduction for the site",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="Homepage image",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
