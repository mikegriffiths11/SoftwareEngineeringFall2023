from django.db import models

class Beverage(models.Model):
    name = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)