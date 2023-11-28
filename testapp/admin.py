from django.contrib import admin
from .models import Item, MenuItem, Through

# Register your models here.

# Item Admin
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'quantity', 'slug']
    search_fields = ['name', 'slug']

# MenuItem Through Admin
class ThroughAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'item', 'quantity']
    search_fields = ['menu_item__name', 'item__name']

class ThroughInline(admin.TabularInline):
    model = Through
    fk_name = 'menu_item'
    extra = 1

# MenuItem Admin
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'selling_price', 'markup']
    search_fields = ['name']
    filter_horizontal = ['items']
    inlines = [ThroughInline]

    def price_of_items(self, obj):
        return obj.price_of_items()

    price_of_items.short_description = 'Total Price of Items'

# Register models with their respective admins
admin.site.register(Item, ItemAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Through, ThroughAdmin)
