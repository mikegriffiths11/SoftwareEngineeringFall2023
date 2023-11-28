from django.db import models


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)



# Create your models here.

class login(models.Model):
    employee_ID = models.TextField()

class shipping(models.Model):
    address = models.TextField()
    Postal_code = models.TextField()
    payment = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(man_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
