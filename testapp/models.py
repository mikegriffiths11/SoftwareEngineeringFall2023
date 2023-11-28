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
#need to make two classes each

#I'm going to mess around a bit

# item
#login (user id)
#food
#beverage
#utility
#shipping

#order

class Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    type = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Food(models.Model):
    name = models.TextField()
    description = models.TextField()
    type = models.TextField()




#trying, in class Thurs Nov 16

class MinutesMixIn(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LocationsofItems(MinutesMixIn):
    storenumber = models.TextField()
    room = models.TextField()
    shelf = models.IntegerField()

class NewMessingAround(models.Model):
    testing = models.TextField()

