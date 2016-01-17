from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class GAETestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://localhost:8080/')
        self.assertIn('Ghost Name Picker', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
