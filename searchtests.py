import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  # Asegúrate de importar By
from selenium.webdriver.chrome.service import Service

class HomePageTests(unittest. TestCase):
    
    
    def setUp(self):
        #service = Service(executable_path=r"C:\Users\joana\Desktop\chrome-win64\chromedriver.exe")
        self.driver = webdriver.Chrome()  # Inicializa self.driver aquí
        self.driver.get("http://demo-store.seleniumacademy.com/")
        self.driver.maximize_window()
    
    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, "search")
    
    
    def tearDown(self):
        self.driver.quit()
    
if  __name__ == "__main__":
        unittest.main(verbosity=2)
