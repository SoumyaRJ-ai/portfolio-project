from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    blog_body = models.TextField()
    blog_image = models.ImageField(upload_to='images/')