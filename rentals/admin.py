from django.contrib import admin

from rentals.models import Property, Category

admin.site.register(Category)
admin.site.register(Property)
