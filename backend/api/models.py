from django.db import models

# Create your models here.

class Student(models.Model):
    
    sid = models.IntegerField(null=False )
    name = models.CharField(max_length=10 , null=False)
    age = models.IntegerField( null=False )

