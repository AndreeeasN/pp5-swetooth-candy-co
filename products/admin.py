from django.contrib import admin
from .models import Product, Category, Brand, ProductTag, ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'brand',
        'image',
    )
    search_fields = ['sku', 'name', 'brand__name']
    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )
    ordering = ('name',)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'search_visible',
    )
    ordering = ('name',)


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'variant_price',
    )
    ordering = ('name',)
