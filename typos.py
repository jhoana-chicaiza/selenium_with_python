import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By

class Typos(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, "Typos").click()
        
    def test_find_typo(self):
        driver= self.driver
        
        paragraph_to_check = driver.find_element(By.XPATH, '//*[@id="content"]/div/p[2]')
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        
        
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."
        
        while text_to_check!= correct_text:
            paragraph_to_check = driver.find_element(By.XPATH, '//*[@id="content"]/div/p[2]')
            text_to_check = paragraph_to_check.text
            driver.refresh()
        
        while not found:
            if text_to_check == correct_text:
                tries== 1
                driver.refresh()
                found = True
        self.assertEqual(found,True)
        
        print(f"It took {tries} tries to find the typo")
        
    def tearDown(self):
        self.driver.quit() 
        
if __name__ == "__main__":
    unittest.main(verbosity=2)