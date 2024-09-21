from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuTestCase(TestCase):
    def test_get_item(self):
        menu = Menu.objects.create(title="Pizza", price=80, inventory=100)
        self.assertEqual(str(menu), "Pizza : 80")
