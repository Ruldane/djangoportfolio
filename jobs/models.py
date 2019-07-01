from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, default='SOME STRING')
    company = models.CharField(max_length=50, default='SOME STRING')
    date_to_date = models.CharField(max_length=50, default='SOME STRING')
    summary = models.TextField(max_length=800, default='SOME STRING')

    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:0]

class Formation(models.Model):
    date_to_date = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=800)

    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:0]
