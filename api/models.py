from django.db import models

class Seller(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    password = models.CharField(max_length=50)    

class Client(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    password = models.CharField(max_length=50)   

class Admin(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50) 