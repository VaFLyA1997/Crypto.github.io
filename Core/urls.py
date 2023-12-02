from django.urls import path
from . import views


urlpatterns = [
    path('shop/<int:pk>/', views.ShopView, name='Shop'),
    path('service/<int:pk>/', views.ServiceView, name='Service'),
    path('farm/<int:pk>/', views.FarmView, name='Farm'),
    path('heating/<int:pk>/', views.HeatingView, name='Heating'),
    path('product/', views.ProductView, name='Product'),
    path('productService/', views.ProductServiceView, name='ProductService'),
    # path('', views.MainView, name="Main")
]