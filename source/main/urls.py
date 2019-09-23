
from django.contrib import admin
from django.urls import path

from webapp.views import index_view, item_view, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='main'),
    path('item/<int:pk>/', item_view, name='item_view'),
    path('item/search/', search_view, name='item_search')
]
