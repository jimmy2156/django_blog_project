from django.db import models
from datetime import date
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    tag = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.tag}"
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=900)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag, null=False, default="")
    slug = models.SlugField(unique=True, db_index=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("single_blog", args=[self.slug])
    def __str__(self) -> str:
        return f"{self.title} {self.date}"
    
