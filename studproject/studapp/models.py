from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.stuid}-{self.stuname}'

