from django.contrib import admin
from .models import Product

#allow products to be managed from the admin portal
admin.site.register(Product)
