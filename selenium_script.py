from selenium import webdriver
import unittest
import time

class Test_Data_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # User goes to Webpage and expects to see Data in the title
    def test_data_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000/signup/data')
        self.assertIn("Data", self.driver.title,  "Webpage Name does not match expected") 

    def tearDown(self):
        self.driver.quit()

class Test_SignUp_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # User goes to SignUp Webpage and expects to see Sign Up in the title
    def test_signup_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000/signup/signup')
        self.assertIn("Sign Up", self.driver.title, "Webpage Name does not match expected") 

    # User expects the Sign Up page to contain a signup button labelled 'Sign Up Here'
    def test_signup_page_contains_signup_button(self):
        self.driver.get('http://127.0.0.1:8000/signup/signup')
        self.driver.find_element_by_tag_name('button')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()