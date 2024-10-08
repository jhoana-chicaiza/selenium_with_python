import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #service = Service(executable_path=r"C:\Users\joana\Desktop\chrome-win64\chrome-win64\chrome.exe")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
    
    
    def test_hello_world(self):
        driver = self.driver
        driver.get("http://www.platzi.com")
        
    def test_visit(self):
        self.driver.get('https://www.wikipedia.org')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reporte', report_name='hello-world-report'))
