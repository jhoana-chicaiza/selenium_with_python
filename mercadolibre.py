import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestingMercadoLibre(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()
        
    def test_search_ps4(self):
        driver = self.driver
        
        # Esperar a que el selector de país esté visible y hacer clic
        country = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'CO'))
        )
        country.click()
        
        # Esperar a que el campo de búsqueda esté visible
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'as_word'))
        )
        search_field.clear()
        search_field.send_keys('ps4')
        search_field.submit()
        
        # Esperar a que el filtro de ubicación esté visible y hacer clic
        location = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Bogotá D.C.'))
        )
        driver.execute_script("arguments[0].click();", location)
        
        # Esperar a que el filtro de condición esté visible y hacer clic
        condition = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Nuevo'))
        )
        driver.execute_script("arguments[0].click();", condition)
        
        # Esperar a que el menú de orden esté visible y hacer clic
        order_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'andes-dropdown__trigger'))
        )
        order_menu.click()
        
        # Esperar a que la opción de mayor precio esté visible y hacer clic
        higher_price = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#\:R2m55e6\:-menu-list-option-price_desc > div'))
        )
        higher_price.click()
        
        articles = []
        prices = []
        
        # Recopilar los nombres y precios de los primeros 5 artículos
        for i in range(5):
            article_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="root-app"]/div/div[3]/section/ol/li[{i+1}]/div/div/div[2]/a'))
            ).text
            articles.append(article_name)
            article_price = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="root-app"]/div/div[3]/section/ol/li[{i+1}]/div/div/div[2]/div[2]'))
            ).text
            prices.append(article_price)
        
        print(articles, prices)
            
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
