from django.db import models
from django.forms import ModelForm, Textarea
# Create your models here.
class Employee(models.Model):
    
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mob=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    doj=models.DateField()
    accno=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=100)
    payscale=models.CharField(max_length=100)

class superadmin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Meta:
    db_table='employee'