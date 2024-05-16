from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']


@admin.register(StockProduct)
class StockProduct(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']
    list_filter = ['quantity']

