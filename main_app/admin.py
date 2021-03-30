from django.contrib import admin
from .models import Subscription, Product, Invoice


admin.site.register(Subscription)
admin.site.register(Product)
admin.site.register(Invoice)
