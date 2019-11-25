from django.test import TestCase
from django.urls import resolve
from landing.views import landing_view
from secnet import settings

# Create your tests here.
class ConfigTest(TestCase):
	
	def test_landing_page_server_response(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
	
	def test_root_url_resolves_to_landing_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, landing_view)
	
