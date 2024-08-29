import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest. TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("Platzi")
        
        
        self.assertEqual('Platzi', google.keyword)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
if  __name__ == "__main__":
    unittest.main(verbosity=2)
        