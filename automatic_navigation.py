import unittest 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class NavigationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver =self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')
        
    def test_browser_navigation(self):
        driver = self.driver
        search_field= driver.find_element(By.NAME,'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()
        
        driver.back()
        time.sleep(3)
        driver.forward()
        driver.refresh()
        
    def tearDown(self):
        self.driver.quit() 
        
if  __name__ == "__main__":
    unittest.main(verbosity=2)