from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)    
    city = models.CharField(max_length=100)

   
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='groups')

    def __str__(self):
        return self.name