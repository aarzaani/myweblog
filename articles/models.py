from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # tumbnail
    # author
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:50]+'...'
# Create your models here.
