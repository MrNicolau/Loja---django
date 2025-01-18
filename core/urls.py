from django.contrib import admin
from django.urls import path
from app.views import ProductListView, ProductCreateView, ProductDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='product-list'),
    path('create/',ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/',ProductDetailView.as_view(), name='product-detail')
]
