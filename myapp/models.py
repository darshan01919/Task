from django.db import models

# Create your models here.


class User_table(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
    Phone=models.BigIntegerField()
    Data_submitted_at=models.DateTimeField(auto_now_add=True,null=True)
