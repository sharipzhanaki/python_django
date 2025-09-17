"""
В этом модуле лежат различные наборы представлений.

Разные view интернет-магазина: по товарам, заказам и т.д.
"""

import logging
from timeit import default_timer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.syndication.views import Feed

from .forms import GroupForm, ProductForm
from .models import Product, Order, ProductImage
from .serializers import OrderSerializer


log = logging.getLogger(__name__)


class ShopIndexView(View):
    # @method_decorator(cache_page(60 * 2))
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
            "items": 2,
        }
        # log.debug("Products for shop index: %s", products)
        # log.info("Rendering shop index")
        print("shop index context", context)
        return render(request, 'shopapp/shop-index.html', context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class ProductDetailsView(DetailView):
    template_name = "shopapp/product-details.html"
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    #model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    # def test_func(self):
    #     # return self.request.user.groups.filter(name='secret-group').exists()
    #     return self.request.user.is_superuser

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shopapp:products_list")
    permission_required = "shopapp.add_product"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    # fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"
    form_class = ProductForm

    def test_func(self):
        user = self.request.user
        product = self.get_object()
        return (
                user.is_superuser or (user.has_perm("shopapp.change_product") and
                                      product.created_by == user)
        )
        # return self.request.user.groups.filter(name='secret-group').exists()

    def handle_no_permission(self):
        return HttpResponse(f"You don't have permission to change product details!", status=403)

    def get_success_url(self):
        return reverse("shopapp:product_details", kwargs={"pk": self.object.pk},)

    def form_valid(self, form):
        response = super().form_valid(form)
        images = form.files.getlist("images")
        for image in images:
            ProductImage.objects.create(
                product=self.object,
                image=image,
            )

        return response


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        cache_key = "products_data_export"
        products_data = cache.get(cache_key)
        if products_data is None:
            products = Product.objects.order_by('pk').all()
            products_data = [
                {
                    "pk": product.pk,
                    "name": product.name,
                    "price": product.price,
                    "archived": product.archived,
                }
                for product in products
            ]
            cache.set("products_data_export", products_data, 300)
        return JsonResponse({"products": products_data})


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
            .select_related("user")
            .prefetch_related("products")
            .all()
    )


class LatestProductsFeed(Feed):
    title = "Latest Products"
    description = "updates on changed and addition products list"
    link = reverse_lazy("shopapp:products_list")

    def items(self):
        return (
            Product.objects
            .order_by("-created_at")[:10]
        )

    def item_title(self, item: Product):
        return item.name

    def item_description(self, item: Product):
        return item.description[:200]


class OrdersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ["shopapp.view_order", ]
    queryset = (Order.objects.select_related("user").prefetch_related("products"))


class OrderCreateView(CreateView):
    model = Order
    fields = "user", "delivery_address", "products", "promocode"
    success_url = reverse_lazy("shopapp:orders_list")


class OrderUpdateView(UpdateView):
    model = Order
    fields = "user", "delivery_address", "products", "promocode"
    success_url = reverse_lazy("shopapp:orders_list")


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("shopapp:orders_list")


class UserOrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "shopapp/user_orders_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        self.owner = get_object_or_404(User, pk=user_id)
        return Order.objects.select_related("user").filter(user=self.owner)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = self.owner
        return context


def export_user_orders_view(request, user_id: int):
    cache_key = f"user_{user_id}_orders_export"
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data, safe=False)

    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(user=user).order_by("pk").select_related("user")
    serializer = OrderSerializer(orders, many=True)

    cache.set(cache_key, serializer.data, timeout=60 * 5)
    return JsonResponse(serializer.data, safe=False)
