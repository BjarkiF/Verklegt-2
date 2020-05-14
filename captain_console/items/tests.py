from django.test import TestCase
from items.models import Item


class AnimalTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="lion", description="roar", price=0, category_id=0, manufacturer_id=1)
        Item.objects.create(name="cat", description="meow", price=0, category_id=2, manufacturer_id=2)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Item.objects.get(name="lion")
        cat = Item.objects.get(name="cat")
        self.assertEqual(lion.name, 'lion')
        self.assertEqual(cat.name, 'cat')