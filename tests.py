import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestFrontend(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
         

    def tearDown(self):
        self.driver.quit()
        
        
    def testpages(self):
        
        
        def test_add_button(self):
            self.driver.get('http://127.0.0.1:5000/')
            add_button=self.driver.find_element(By.CLASS_NAME,'addbutton')
            
            add_button.click()
            
            self.assertEqual('http://127.0.0.1:5000/add_button?',self.driver.current_url)
            
        def test_add_page(self):
            self.driver.get('http://127.0.0.1:5000/add_button?') 
            email_input = self.driver.find_element(By.ID, 'email')
            fname_input = self.driver.find_element(By.ID, 'fname')
            lname_input = self.driver.find_element(By.ID, 'lname')
            mobile_input = self.driver.find_element(By.ID, 'mobile')
            dob_input = self.driver.find_element(By.ID, 'dob')
            submit_button = self.driver.find_element(By.CLASS_NAME, 'submit')

            email_input.send_keys('test@example.com')
            fname_input.send_keys('John')
            lname_input.send_keys('Doe')
            mobile_input.send_keys('1234567890')
            dob_input.send_keys('2000-01-01')

        
            submit_button.click()

            self.assertEqual('http://127.0.0.1:5000/', self.driver.current_url)
        
        def test_edit_button(self):
            self.driver.get('http://127.0.0.1:5000/')
            edit_button=self.driver.find_element(By.CLASS_NAME,'editbutton')
            
            edit_button.click()
            
            self.assertEqual('http://127.0.0.1:5000/edit/test@example.com?',self.driver.current_url)
        
        def test_delete_button(self):
            self.driver.get('http://127.0.0.1:5000/')
            edit_button=self.driver.find_element(By.CLASS_NAME,'deletebutton')
            
            edit_button.click()
            
            self.assertEqual('http://127.0.0.1:5000/',self.driver.current_url)
            
        def test_edit_page(self):
            self.driver.get('http://127.0.0.1:5000/edit/hari@gmail.com?') 
    
            submit_button = self.driver.find_element(By.CLASS_NAME, 'submit')

        
            submit_button.click()

            self.assertEqual('http://127.0.0.1:5000/', self.driver.current_url)
            
        test_add_button(self)
        test_add_page(self)
        test_edit_button(self)
        test_delete_button(self)
        test_edit_page(self)

if __name__ == '__main__':
    unittest.main()
