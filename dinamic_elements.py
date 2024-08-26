import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By

class DinamicElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver =self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, "Disappearing Elements").click()
        
    def test_name_elements(self):
        driver= self.driver
        options=[]
        menu =5
        tries=1
        
        while len(options)<5:
            options.clear()
            
            for i in range(1,menu+1):
                try: 
                    option_name = driver.find_element(By.XPATH,f'//*[@id="content"]/div/ul/li[{i}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number{i} is NOT FOUND")
                    tries +=1
                    driver.refresh()
                    break 
        print(f"Finished in {tries} tries")
                    
    def tearDown(self):
        self.driver.quit() 
        
if  __name__ == "__main__":
    unittest.main(verbosity=2)