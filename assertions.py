import unittest 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver =self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()
        
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.send_keys('salt shaker')
        search_field.submit()
        
        products = driver.find_elements(By.XPATH,'//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1,len(products))
        
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
        
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
    
    def tearDown(self):
        self.driver.quit() 
    
    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False 
        return True
    
    if  __name__ == "__main__":
        unittest.main(verbosity=2)