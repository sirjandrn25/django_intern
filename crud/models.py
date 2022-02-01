from django.db import models

# Create your models here.

class Student(models.Model):
    class MajorChoices(models.TextChoices):
        SCIENCE = "S","Science"
        MANAGEMENT = "M","Management"

    class GradeChoices(models.TextChoices):
        PLUS_TO = "+2","+2"
        BACHLER = "B","Bachler"

    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    grade = models.CharField(max_length=10,choices=GradeChoices.choices,default=GradeChoices.PLUS_TO)
    major = models.CharField(max_length=12,choices=MajorChoices.choices,default=MajorChoices.SCIENCE)

    def __str__(self):
        return self.full_name