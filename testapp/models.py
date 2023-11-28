from django.db import models
from django.db import models


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.IntegerField()
    email = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return str(self.first_name) + str(self.last_name)




# Create your models here.

# this is the lazy way of dealing with this; need to eventually make it join tables
# (things like booleans and each option)
class StockedCategories(models.Model):
    entrees = models.JSONField()
    burgers = models.JSONField()
    sauces = models.JSONField()
    drinks = models.JSONField()


# same as above class. Need to fix the JSONField into conjoined tables
class FoodOrder(models.Model):
    drinks = models.IntegerField
    orderBurger = models.JSONField
    sauce = models.TextChoices("1,2,3""Sweet,Sour,Spicy")
    orderEntrees = models.JSONField
