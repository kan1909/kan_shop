from django.contrib import admin

from apps.orders.models import OrderEntity, OrderPhysical, Product, ProductEntity


class ProductImageAdmin(admin.TabularInline):
    model = Product
    extra = 1


class OrderPhysicalAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = (
        'user', 'cart', 'fname', 'lname',
        'email', 'number', 'order_id', 'city',
        'address', 'created', 'total'
    )
    list_filter = (
        'fname', 'lname', 'number', 'order_id',
        'city', 'address', 'created', 'total'
    )
    search_fields = (
        'fname', 'lname', 'number', 'order_id',
        'city', 'address',
    )



class ProductEntityImageAdmin(admin.TabularInline):
    model = ProductEntity
    extra = 1


class OrderEntityAdmin(admin.ModelAdmin):
    inlines = [ProductEntityImageAdmin]
    list_display = (
        'user', 'cart', 'fname', 'lname',
        'email', 'number', 'order_id', 'city',
        'address', 'inn', 'kpp', 'contact_face',
        'created', 'total',
    )
    list_filter = (
        'user', 'cart', 'fname', 'lname',
        'email', 'number', 'order_id', 'city',
        'address', 'inn', 'kpp', 'contact_face',
        'created', 'total',
    )
    search_fields = (
        'fname', 'lname', 'number', 'order_id',
        'city', 'address', 'inn', 'kpp', 'contact_face',
    )


admin.site.register(OrderEntity, OrderEntityAdmin)
admin.site.register(OrderPhysical, OrderPhysicalAdmin)
