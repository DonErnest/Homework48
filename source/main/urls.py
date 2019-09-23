
from django.contrib import admin
from django.urls import path

from webapp.views import index_view, item_view, search_view, add_view, update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='main'),
    path('item/<int:pk>/', item_view, name='item_view'),
    path('item/search/', search_view, name='item_search'),
    path('item/add/', add_view, name='item_add'),
    path('item/update/<int:pk>', update_view, name='item_update')
]
