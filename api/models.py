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

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    imageURL = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Product_Details(models.Model):
    description = models.TextField()
    imageURL = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Rating(models.Model):
    count = models.IntegerField()
    rating_number = models.IntegerField()
    comment = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)