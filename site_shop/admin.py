from django.contrib import admin

from site_shop.models import Section, Product, Discount, Order, OrderLine

# Register your models here.
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderLine)