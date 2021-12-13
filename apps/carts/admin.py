from django.contrib import admin

from apps.carts.models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product_item', 'amount')
    list_filter = ('product_item', 'amount')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
