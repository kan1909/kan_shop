from django.contrib import admin
from apps.products.models import ProductItem, ProductImage, Product, ProductSale


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductItemsAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('title', 'price', 'size_chart', 'size', 'quantity', 'color')
    search_fields = ('title', 'price')
    list_filter = ('title', 'price', 'size_chart', 'size', 'quantity',)
    list_max_show_all = 500
    list_per_page = 200


class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'category')
    search_fields = ('article', 'category')
    list_filter = ('article', 'category')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSale)
admin.site.register(ProductItem, ProductItemsAdmin)
