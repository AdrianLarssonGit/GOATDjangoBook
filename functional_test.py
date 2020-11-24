from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrive_it_later(self):
        #Edit has heard about a cool new onlint  to do app. 
        #She goes to check it out
        self.browser.get('http://localhost:8000')

        #She notices the page title and header talking about lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")
        
        #She is invited to enter a to do item right 

if __name__ == '__main__':
    unittest.main()
