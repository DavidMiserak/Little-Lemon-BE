from django.test import TestCase
from .models import Menu


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title='Pizza', price=10.00, inventory=10)
        Menu.objects.create(title='Burger', price=5.00, inventory=20)

    def test_getall(self):
        """
        Ensure we can get all menu items.
        """
        response = self.client.get('/restaurant/menu')

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check the number of menu items
        items = response.json()
        self.assertEqual(len(items), 2)

        # Check the menu item names
        self.assertEqual(items[0]['title'], 'Pizza')
        self.assertEqual(items[1]['title'], 'Burger')

        # Check the menu item prices
        self.assertEqual(items[0]['price'], '10.00')
        self.assertEqual(items[1]['price'], '5.00')

        # Check the menu item inventory
        self.assertEqual(items[0]['inventory'], 10)
        self.assertEqual(items[1]['inventory'], 20)
