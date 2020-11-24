from django.test import TestCase
from lists.views import home_page 
from django.urls import resolve
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_resolves_to_home_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

