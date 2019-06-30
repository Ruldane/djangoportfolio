from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date_pub =  models.DateField(default=timezone.now())
    body = models.TextField(max_length=800)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')