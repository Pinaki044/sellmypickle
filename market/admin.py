from django.contrib import admin
from .models import CAddress, Customer, SHG, Type, Item, Order, OrderItem, Payment

admin.site.register(CAddress)
admin.site.register(Customer)
admin.site.register(SHG)
admin.site.register(Type)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)

