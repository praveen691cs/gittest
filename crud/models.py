from django.db import models

# Create your models here.

class Employee(models.Model):
    #emp_id = models.CharField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=100,unique=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    class Meta:
        db_table='employee'

