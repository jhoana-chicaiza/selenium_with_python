import unittest 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, "Dynamic Controls").click()
        
    def test_dynamic_controls(self):
        driver = self.driver
        
        # Interacción con el checkbox y su botón de eliminación/adición
        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        checkbox.click()
        
        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()
        
        # Esperar hasta que el botón esté disponible para hacer clic de nuevo
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()
        
        # Interacción con el botón de habilitar/deshabilitar
        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()
        
        # Esperar hasta que el campo de texto esté habilitado
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input[type=text]")))
        
        # Interactuar con el campo de texto
        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('Platzi')
        
        # Deshabilitar el campo de texto nuevamente
        enable_disable_button.click()
        
    def tearDown(self):
        self.driver.quit() 
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
