from django.contrib import admin
from .models import Post, Author,Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("title", "date",)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)