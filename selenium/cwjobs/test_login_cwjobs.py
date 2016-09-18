import unittest
from selenium import webdriver
class CwJobsLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://www.cwjobs.co.uk/account/signin"

    def tearDown(self):
        self.driver.close()

    def test_login_succes(self):
        self.driver.get(self.url)
        email = "irinatest@gmail.com"
        password = "test12345"
        self.driver.find_element_by_id("Form_Email").send_keys(email)
        self.driver.find_element_by_id("Form_Password").send_keys(password)
        self.driver.find_element_by_id("btnLogin").click()
        self.assertIn("irinatest's account", self.driver.page_source)

    def test_login_no_email_input(self):
        self.driver.get(self.url)
        password = "123"
        self.driver.find_element_by_id("Form_Email").clear()
        self.driver.find_element_by_id("Form_Password").send_keys(password)
        self.driver.find_element_by_id("btnLogin").click()
        self.assertIn("Please provide an email address", self.driver.page_source)

    def test_login_no_password(self):
        self.driver.get(self.url)
        email = "fakeemail@gmail.com"
        self.driver.find_element_by_id("Form_Email").send_keys(email)
        self.driver.find_element_by_id("Form_Password").clear()
        self.driver.find_element_by_id("btnLogin").click()
        self.assertIn("Please provide a password.", self.driver.page_source)

    def test_login_wrong_email_format(self):
        self.driver.get(self.url)
        email = "irinatest.gmail.com"
        password = "test12345"
        self.driver.find_element_by_id("Form_Email").send_keys(email)
        self.driver.find_element_by_id("Form_Password").send_keys(password)
        self.driver.find_element_by_id("btnLogin").click()
        self.assertIn("Please enter a valid email address.", self.driver.page_source)


if __name__ == "__main__":
    unittest.main()
