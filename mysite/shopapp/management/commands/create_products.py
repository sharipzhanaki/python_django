from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Creates products
    """
    def handle(self, *args, **options):
        self.stdout.write("Create products")

        products_names = [
            {"name": "Laptop", "price": 1999},
            {"name": "Desktop", "price": 2999},
            {"name": "Smartphone", "price": 987},
        ]
        for item in products_names:
            product, created = Product.objects.get_or_create(
                name=item["name"], defaults={"price": item["price"]}
            )
            if not created:
                self.stdout.write(f"Product {product.name} already exists")
            else:
                self.stdout.write(f"Created product {product.name} with price {product.price}")

        self.stdout.write(self.style.SUCCESS("Products created"))
