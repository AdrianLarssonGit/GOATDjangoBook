from django.test import TestCase
# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_return_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        
        
        self.assertTemplateUsed(response, 'home.html')

