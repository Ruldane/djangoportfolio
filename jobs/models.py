from django.db import models
from ckeditor.fields import RichTextField

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, default='SOME STRING')
    company = models.CharField(max_length=50, default='SOME STRING')
    date_to_date = models.CharField(max_length=50, default='SOME STRING')
    summary = RichTextField(default='SOME STRING')

    def __str__(self):
        return self.company

    def body(self):
        return self.summary[:0]

class Formations(models.Model):
    title = models.CharField(max_length=255)
    center_formation = models.CharField(max_length=100)
    date_to_date = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title

class skills(models.Model):
    name_skills = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=800, default='SOME STRING')

    def __str__(self):
        return self.name_skills




