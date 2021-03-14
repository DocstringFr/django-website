from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = "Article"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_words(self):
        return len(self.content.split())

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug})

