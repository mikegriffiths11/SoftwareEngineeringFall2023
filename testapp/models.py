from django.db import models

class TestGit(models.Model):
    testField = models.TextField()

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
<<<<<<< HEAD
    phone = models.IntegerField()
    email = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return str(self.first_name) + str(self.last_name)
=======
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)
>>>>>>> fe6043dd1decfa51a8a7b8c41a46c61b04613dfc


class BaseMixin(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=20)


<<<<<<< HEAD
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
=======
class FoodMixin(models.Model):
    class Meta:
        abstract = True

    calories = models.IntegerField(null=True, blank=True)
    health_rating = models.IntegerField(null=True, blank=True)


class MeatMixin(models.Model):
    class Meta:
        abstract = True
    # meat fields
    types = [
        "beef",
        "pork",
        "chicken"
    ]
    type_choices = [(x, x) for x in types]
    meat_type = models.CharField(choices=type_choices, max_length=10, null=True, blank=True)


class SizeMixin(models.Model):
    class Meta:
        abstract = True
    size_choices = [
        ("s", "small"),
        ("m", "medium"),
        ("l", "large")
    ]
    size = models.CharField(choices=size_choices, max_length=2, null=True, blank=True)

class Location(models.Model):
    aisle = models.IntegerField()
    bay = models.IntegerField()
    shelf = models.IntegerField()

class Item(BaseMixin, FoodMixin, MeatMixin, SizeMixin):
    cost = models.FloatField(default=0)
    instock = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='items')


class MenuItem(BaseMixin):
    selling_price = models.FloatField(default=0)
    items = models.ManyToManyField(Item, through='Through', related_name='menu_items')

    @property
    def price_of_items(self):
        total_price = 0
        for relation in self.through_set.all():
            total_price += relation.item.cost * relation.quantity
        return total_price

    @property
    def markup(self):
        return self.selling_price - self.price_of_items

    def add_item(self, item, quantity):
        # Add the item to the many-to-many relationship with the through table
        self.items.through.objects.create(item=item, quantity=quantity)

    def change_quantity_of_item(self, item, quantity):
        self.items.through.objects.get(item=item).update(quantity=quantity)

    def remove_item(self, item):
        self.items.through.objects.get(item=item).delete()


class ItemInAMenuItem(models.Model):
    class Meta:
        # Enforce uniqueness on the combination of item and menu_item
        constraints = [
            models.UniqueConstraint(fields=['item', 'menu_item'], name='unique_item')
        ]

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='mi_through')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='i_through')
    quantity = models.IntegerField(default=1)
>>>>>>> fe6043dd1decfa51a8a7b8c41a46c61b04613dfc

class Beverage(models.Model):
    name = models.TextField()
    quantity = models.IntegerField()
class TestGit(models.Model):
    testField = models.TextField()

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()