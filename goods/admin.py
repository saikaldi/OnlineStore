from django.contrib import admin
from goods.models import Categories, Products
# Register your models here.


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} #to fill   automatically

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
