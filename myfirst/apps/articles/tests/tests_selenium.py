# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Sign Up").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("testpassword12345")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("testpassword12345")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpassword12345")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Add article").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("article")
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("text")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Main").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Articles'])[1]/following::h2[1]").click()
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("comment from aut")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Sign Out").click()
        driver.find_element_by_link_text("Main").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Articles'])[1]/following::h2[1]").click()
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("guest")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("")
        driver.find_element_by_id("grp-content-container").click()
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("grp-content").click()
        driver.find_element_by_xpath("//input[@value='Log in']").click()
        driver.find_element_by_xpath("//div[@id='model-user']/a/strong").click()
        driver.find_element_by_xpath("//table[@id='result_list']/tbody/tr[4]/th").click()
        driver.find_element_by_link_text("testuser").click()
        driver.find_element_by_link_text("Delete").click()
        driver.find_element_by_xpath("//input[@value=\"Yes, I'm sure\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Sign Out").click()
        driver.find_element_by_link_text("Main").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
