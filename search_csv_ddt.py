import csv, unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack


def get_data(file_name):
    rows = []
    with open(file_name,'r') as data_file:
        reader = csv.reader(data_file)
        next (reader,None)
    
        for row in reader:
            rows.append(row)
    return rows
    
@ddt
class SearchCsvDDT(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver =self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        
        
    @data(*get_data('testdata.csv'))
    @unpack
    
    def test_search_ddt(self, search_value, expected_count):
        driver= self.driver
        search_field= driver.find_element(By.NAME,'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()
        
        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')
        
        expected_count= int(expected_count)
        
        if expected_count>0:
            self.assertEqual(expected_count,len(products))
        else:
            message= driver.find_element(By.CLASS_NAME, 'note-msg').text
            self.assertEqual('Your search returns no results.', message)
        print(f'Found {len(products)} products')
        
    def tearDown(self):
        self.driver.quit() 
        
if __name__ == "__main__":
    unittest.main(verbosity=2)