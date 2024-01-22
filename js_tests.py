import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormValidation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
    
        self.driver.quit()

    def test_valid_fname(self):
        self.driver.get('http://127.0.0.1:5000/add_button?')  
        
        input = self.driver.find_element(By.ID,'fname')
        input.send_keys('Testfname')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valfname()')

        error = self.driver.find_element(By.ID,'fnameerror')
        self.assertEqual(error.text, '')

    def test_invalid_fname(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'fname')
        input.send_keys('123')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valfname()')

        error = self.driver.find_element(By.ID,'fnameerror')
        self.assertEqual(error.text, 'Enter only alphabets')
        
    def test_valid_lname(self):
        self.driver.get('http://127.0.0.1:5000/add_button?')  
        
        input = self.driver.find_element(By.ID,'lname')
        input.send_keys('Testlname')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('vallname()')

        error = self.driver.find_element(By.ID,'lnameerror')
        self.assertEqual(error.text, '')
        
    def test_invalid_lname(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'lname')
        input.send_keys('123')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('vallname()')

        error = self.driver.find_element(By.ID,'lnameerror')
        self.assertEqual(error.text, 'Enter only alphabets')
        
    def test_valid_mobile(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'mobile')
        input.send_keys('1234567892')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valmob()')

        error = self.driver.find_element(By.ID,'mobileerror')
        self.assertEqual(error.text, '')
        
    def test_invalid_mobile(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'mobile')
        input.send_keys('123')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valmob()')

        error = self.driver.find_element(By.ID,'mobileerror')
        self.assertEqual(error.text, 'Enter valid mobile number')
        
    def test_valid_email(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'email')
        input.send_keys('example@gmail.com')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valemail()')

        error = self.driver.find_element(By.ID,'emailerror')
        self.assertEqual(error.text, '')
        
    def test_invalid_email(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'email')
        input.send_keys('example')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valemail()')

        error = self.driver.find_element(By.ID,'emailerror')
        self.assertEqual(error.text, 'Enter valid email ID') 
    
    def test_email_exists(self):
        self.driver.get('http://localhost:5000/add_button?')  

        input = self.driver.find_element(By.ID,'email')
        input.send_keys('hari@gmail.com')
        input.send_keys(Keys.TAB)

        self.driver.execute_script('valemail()')

        email_error = self.driver.find_element(By.ID,'emailerror')
        self.assertEqual(email_error.text, 'Email already exists')   
        
    # def test_valid_date(self):
    #     self.driver.get('http://localhost:5000/add_button?')  

    #     input = self.driver.find_element(By.ID,'dob')
    #     date_value = '2002-04-01'
    #     self.driver.execute_script("arguments[0].value = arguments[1];", input, date_value)

    #     input.send_keys(Keys.TAB)

    #     self.driver.execute_script('valdate()')

    #     error = self.driver.find_element(By.ID,'doberror')
    #     self.assertEqual(error.text, '')   
        
    # def test_invalid_date(self):
    #     self.driver.get('http://localhost:5000/add_button?')  

    #     date_input = self.driver.find_element(By.ID, 'dob')

    #     date_input.clear()
    #     date_input.click()

    #     date_element_xpath = '//td[text()="08-09-2023"]'

    #     try:
    #         date_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, date_element_xpath)))
    #     except Exception as e:
    #         print(f"Failed to locate the date element: {e}")
            
    #     action = ActionChains(self.driver)
    #     action.move_to_element(date_element).click().perform()
    #     self.driver.execute_script('valdate()')

    #     error = self.driver.find_element(By.ID,'doberror')
    #     self.assertEqual(error.text, 'Enter valid date')  
    
    def test_check(self):
        self.driver.get('http://localhost:5000/add_button?') 
        
        input = self.driver.find_element(By.ID,'email')
        input.send_keys(Keys.TAB)
        
        input = self.driver.find_element(By.ID,'fname')
        input.send_keys(Keys.TAB)
        
        input = self.driver.find_element(By.CLASS_NAME,'submit')
        input.click()
        
        self.driver.execute_script('check()')
        
        self.assertEqual('http://localhost:5000/add_button?', self.driver.current_url)
   
    def test_valid_emailedit(self):
        
        self.driver.get('http://127.0.0.1:5000/edit/hari@gmail.com?') 
        
        input = self.driver.find_element(By.ID,'email')
        input.clear()
        input.send_keys('haripriya@gmail.com')
        input.send_keys(Keys.TAB)
        
        self.driver.execute_script('valemailedit()')
        
        error = self.driver.find_element(By.ID,'emailerror')
        self.assertEqual(error.text,'')
        
    def test_invalid_emailedit(self):
        
        self.driver.get('http://127.0.0.1:5000/edit/hari@gmail.com?') 
        
        input = self.driver.find_element(By.ID,'email')
        input.clear()
        input.send_keys('invalid')
        input.send_keys(Keys.TAB)
        
        self.driver.execute_script('valemailedit()')
        
        error = self.driver.find_element(By.ID,'emailerror')
        self.assertEqual(error.text,'Enter valid email ID')      
        
if __name__ == '__main__':
    unittest.main()
