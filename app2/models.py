from django.db import models

# Create your models here.
class registerdetails(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    mobile=models.BigIntegerField()
    dateofbirth=models.DateField()
    password=models.CharField(max_length=40)
