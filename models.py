from django.db import models

# Create your models here.
class log(models.Model):
    email= models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    usertype= models.CharField(max_length=100)
    def __str__(self):
        return self.email
class accountant(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    contact=models.CharField(max_length=20)
    def __str__(self):
        return self.email
class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    collegeid=models.CharField(max_length=20,unique=True)
    sex=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    branch=models.CharField(max_length=60)
    semester=models.CharField(max_length=5)
    fee=models.IntegerField()
    paid=models.IntegerField()
    due=models.IntegerField()
    address=models.CharField(max_length=200)
    contact=models.CharField(max_length=100)
    date=models.CharField(max_length=12)
    def __str__(self):
        return self.collegeid