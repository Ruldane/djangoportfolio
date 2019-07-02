from django.db import models
from django.utils import timezone
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date_pub =  models.DateField(default=timezone.now())
    body = models.TextField(max_length=800)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]







