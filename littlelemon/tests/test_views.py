from django.test import TestCase, Client
from restaurant.models import *
from restaurant.serializers import *
import json

class MenuViewTest(TestCase):
    def setup(self):
        menu_item = Menu.objects.create(title="IceCream", price=8.0, inventory=50)
        
    def test_getall(self):
        # client = Client()
        # response = client.get('restaurant/Menu')
        menu = Menu.objects.all()
        menu_serializer = MenuSerializer(menu)
        self.assertEqual(menu, menu_serializer.data)
        