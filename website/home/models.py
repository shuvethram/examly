from django.db import models

# Create your models here.
class student_id(models.Model):
    usrname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class courses(models.Model):
    name = models.CharField(max_length=50)