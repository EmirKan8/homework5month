from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.product_list),
    path('api/v1/products/<int:id>/', views.product_detail),
    path('api/v1/category/', views.category_list),
    path('api/v1/category/<int:id>/', views.category_detail),
    path('api/v1/review/', views.review_list),
    path('api/v1/review/<int:id>/', views.review_detail),
]
