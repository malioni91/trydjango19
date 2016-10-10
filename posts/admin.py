from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp"]
    list_filter = ["timestamp"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin) # Admin function that register the Post model into Admin site.
