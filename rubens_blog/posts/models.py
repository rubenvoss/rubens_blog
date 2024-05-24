from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    slug = models.SlugField(max_length=200, blank=False, unique=True)

    def get_slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)
    
    