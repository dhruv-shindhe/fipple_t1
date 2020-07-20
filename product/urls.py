from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', views.home, name='product-home'),
    path('<str:name>/store1', views.my_products,name='my-products'),
    path('about/', views.about,name='product-about'),
    path('product/<int:pk>', ProductDetailView.as_view(),name='product-detail'),
    path('product/new', ProductCreateView.as_view(),name='product-create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(),name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(),name='product-delete'),
]
