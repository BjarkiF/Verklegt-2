from django.test import TestCase
from users.views import register
# Create your tests here.


class UsersTestCase(TestCase):
    def test_register(self):
        register(request.method = 'POST')
