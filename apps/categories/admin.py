from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from apps.categories.models import Category


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title']
    list_display_links = ['indented_title']
    readonly_fields = ['name']
    search_fields = ('title', 'parent')
    list_filter = ('title', 'parent')


admin.site.register(Category, CategoryAdmin)
