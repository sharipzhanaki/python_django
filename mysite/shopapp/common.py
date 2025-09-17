from csv import DictReader
from io import TextIOWrapper

from shopapp.models import Product, Order


def save_csv_products(file, encoding):
    """
    Сохраняет товары из CSV файла.
    :param file:
    :param encoding:
    :return:
    """
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    products = [
        Product(**row)
        for row in reader
    ]
    Product.objects.bulk_create(products)
    return products


def save_csv_orders(file, encoding):
    """
    Сохраняет заказы из CSV файла.
    :param file:
    :param encoding:
    :return:
    """
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    created_orders = []
    for row in reader:
        user_id = int(row["user_id"])
        product_ids_raw = row.get("product_ids", "").strip()

        if not product_ids_raw:
            continue

        product_ids = [
            int(pid.strip())
            for pid in product_ids_raw.split(",")
            if pid.strip().isdigit()
        ]

        if not product_ids:
            continue

        order = Order.objects.create(
            user_id=user_id,
            delivery_address=row.get("delivery_address", ""),
            promocode=row.get("promocode", ""),
        )
        order.products.set(product_ids)
        created_orders.append(order)

    return created_orders
