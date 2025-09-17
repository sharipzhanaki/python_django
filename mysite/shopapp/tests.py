from django.test import TestCase
from .models import Order
from django.urls import reverse
from django.contrib.auth.models import User, Permission

# Create your tests here.
class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test_user", password="test_pass")
        view_perm = Permission.objects.get(codename="view_order")
        cls.user.user_permissions.add(view_perm)

    def setUp(self):
        self.client.login(username="test_user", password="test_pass")
        self.order = Order.objects.create(
            user=self.user,
            delivery_address="Test Street 12",
            promocode="TEST2025",
        )

    def tearDown(self):
        self.order.delete()

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()

    def test_order_details(self):
        response = self.client.get(
            reverse("shopapp:order_details", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertEqual(response.context["order"].pk, self.order.pk)
