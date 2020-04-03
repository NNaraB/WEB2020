from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'api'

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False), name = "index"),
    path('api/', views.index, name = "index"),
    path('api/categories/', views.categories, name = "categories"),
    path('api/categories/<int:category_id>/', views.detail, name = "detail") ,
    path('api/categories/<int:category_id>/products/', views.products, name = "products") ,
    path('api/products/<int:product_id>', views.product_detail, name = "product_detail")
]