from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    blog_body = models.TextField()
    blog_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.blog_body[:100]

    def date(self):
        return self.published_date.strftime('%b %e %Y')