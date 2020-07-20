from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import StoreCreateView, StoreDetailView, StoreDeleteView, StoreUpdateView


urlpatterns = [
    path('<str:name>/store2', views.mystore,name='my-store'),
    path('', views.home, name='store-home'),
    path('new/', StoreCreateView.as_view(), name='store-create'),
    path('<int:pk>', StoreDetailView.as_view(), name='store-detail'),
    path('<int:pk>/delete', StoreDeleteView.as_view(), name='store-delete'),
    path('<int:pk>/update', StoreUpdateView.as_view(), name='store-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
