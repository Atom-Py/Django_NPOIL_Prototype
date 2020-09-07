from django.contrib import admin
from .models import Distributor,Category,Fuel

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'slug', 'price']
    prepopulated_fields = {'slug': ('name', 'distributor')}
