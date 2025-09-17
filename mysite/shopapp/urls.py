from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import ProductViewSet, OrderViewSet
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductsListView,
    ProductDetailsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    LatestProductsFeed,
    ProductsDataExportView,
    OrdersListView,
    OrdersDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    UserOrdersListView,
    export_user_orders_view,
)

app_name = "shopapp"

routers = DefaultRouter()
routers.register("products", ProductViewSet)
routers.register("orders", OrderViewSet)


urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("api/", include(routers.urls)),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/latest/feed/", LatestProductsFeed(), name="products_feed"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/export/", ProductsDataExportView.as_view(), name="products-export"),
    path("products/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_archive"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>", OrdersDetailView.as_view(), name="order_details"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    path("users/<int:user_id>/orders/", UserOrdersListView.as_view(), name="users_orders"),
    path("users/<int:user_id>/orders/export/", export_user_orders_view, name="users_orders_export")
]
