from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.base,name='base'),
    path('load_stock_group',views.load_stock_group,name='load_stock_group'),
    path('load_stock_category',views.load_stock_category,name='load_stock_category'),
    path('load_stock_item',views.load_stock_item,name='load_stock_item',)


]