from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=50)
    date_to_date = models.CharField(max_length=50)
    summary = models.CharField(max_length=800)

    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:100]