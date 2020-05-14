from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from items.models import Item

#
# class ItemTestCase(APITestCase):
#     def test_create_item(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('items')
#         data = {'name': 'DabApps'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Item.objects.count(), 1)
#         self.assertEqual(Item.objects.get().name, 'DabApps')
