from django.contrib import admin

# Register your models here.
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "slug",
        "author",
        "date",
    )
    list_editable = ("published",)
