from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(null=True, max_length=20)
