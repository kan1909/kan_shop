from django.contrib import admin
from apps.favorites.models import Favorite


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'products')
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(Favorite)
