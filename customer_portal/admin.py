from django.contrib import admin
from .models import Customer, Order

# Register models so they appear in the admin
admin.site.register(Customer)
admin.site.register(Order)
