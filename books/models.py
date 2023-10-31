from django.db import models

# Create your models here.
class Book(models.Model):
    title: models.CharField = models.CharField(max_length=200)]]9767
    author: models.CharField = models.CharField(max_length=100)
    publication_date: models.DateField = models.DateField()
    isbn: models.CharField = models.CharField(max_length=20)
    summary: models.TextField = models.TextField()
