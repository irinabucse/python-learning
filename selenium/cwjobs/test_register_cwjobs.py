import os
import unittest
from random import randint

from selenium import webdriver


class RegisterCwjobs(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome("K:\Downloads\chromedriver.exe")
        self.driver = webdriver.Firefox()

    # def tearDown(self):
    #     self.driver.close()

    def test_register_cwjobs_succes(self):
        self.driver.get("https://www.cwjobs.co.uk/account/register")
        firstName = "irinatest"
        firstNameElement = self.driver.find_element_by_id("firstname")

        surname = "test"
        surNameElement = self.driver.find_element_by_id("surname")

        emailadress = "irinatest" + str(randint(10000, 1000000000)) + "@gmail.com"
        emailadresselement = self.driver.find_element_by_id("email")

        localCv = os.getcwd() + "\\assets\\test_cv.docx"
        localCvElement = self.driver.find_element_by_id("localCv")

        eligibilityUkYesElement = self.driver.find_element_by_css_selector("label[for=eligibilityUkYes]")
        eligibilityUkNoElement = self.driver.find_element_by_css_selector("label[for=eligibilityUkNo]")
        eligibilityEuYesElement = self.driver.find_element_by_css_selector("label[for=eligibilityEuYes]")
        eligibilityEuNoElement = self.driver.find_element_by_css_selector("label[for=eligibilityEuNo]")

        highest_level_education = "GCSE/GNVQ/O levels"
        highest_level_education_element = self.driver.find_element_by_id("ddlEducation")

        most_recent_job_title = "test"
        most_recent_job_title_element = self.driver.find_element_by_id("currentJobTitle")

        recent_salary_annual = "10000"
        recent_salary_annual_element = self.driver.find_element_by_id("rdoAnnualRate")

        recent_salary_daily = "40"
        recent_salary_daily_element = self.driver.find_element_by_id("rdoDailyRate")

        recent_salary_hourly = "5"
        recent_salary_hourly_element = self.driver.find_element_by_id("rdoHourlyRate")

        recent_salary_none_element = self.driver.find_element_by_id("rdoNoRate")

        create_password = "test12345"
        create_password_element = self.driver.find_element_by_id("password")

        confirm_password = "test12345"
        confirm_password_element = self.driver.find_element_by_id("confirmpassword")

        firstNameElement.send_keys(firstName)
        surNameElement.send_keys(surname)
        emailadresselement.send_keys(emailadress)

        localCvElement.send_keys(localCv)

        eligibilityUkYesElement.click()
        eligibilityEuYesElement.click()

        highest_level_education_element.send_keys(highest_level_education)

        self.driver.find_element_by_css_selector(
            "label[for=" + recent_salary_none_element.get_attribute("id") + "]").click()

        most_recent_job_title_element.send_keys(most_recent_job_title)

        # recent_salary_annual_element.send_keys(recent_salary_annual)
        # recent_salary_daily_element.send_keys(recent_salary_daily)
        # recent_salary_hourly_element.send_keys(recent_salary_hourly)

        create_password_element.send_keys(create_password)
        confirm_password_element.send_keys(confirm_password)
        self.driver.find_element_by_id("register").click()

        self.assertIn("Thanks for registering", self.driver.page_source)

    if __name__ == "__main__":
        unittest.main()
