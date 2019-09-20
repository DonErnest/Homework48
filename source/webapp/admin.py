from django.contrib import admin

from webapp.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'amount', 'price']
    list_filter = ['name', 'description', 'category', 'amount', 'price']
    search_fields = ['name', 'description','category','price']
    fields = ['name', 'description', 'category','amount', 'price']


admin.site.register(Item, ItemAdmin)