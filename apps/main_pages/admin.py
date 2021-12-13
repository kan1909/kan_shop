from django.contrib import admin

from apps.main_pages.models import MainPage


class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'name',)
    readonly_fields = ['name']
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(MainPage, MainPageAdmin)
