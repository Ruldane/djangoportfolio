from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date_pub =  models.DateField(default=timezone.now())
    body = RichTextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]







gi