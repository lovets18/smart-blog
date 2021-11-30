# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UserTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_user(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Sign Up").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password1").click()
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("testpas4879")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Sign up'])[1]/following::form[1]").click()
        driver.find_element_by_id("id_password2").click()
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("testpas4879")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Sign up'])[1]/following::form[1]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpas4879")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Add article").click()
        #driver.find_element_by_link_text("become an author").click()
        driver.find_element_by_link_text("Sign Out").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpas4879")
        driver.find_element_by_link_text("Main").click()
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpas4879")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("grp-content").click()
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        driver.find_element_by_xpath("//input[@value='Log in']").click()
        driver.find_element_by_xpath("//div[@id='model-user']/a/strong").click()
        driver.find_element_by_link_text("testuser").click()
        driver.find_element_by_id("id_is_staff").click()
        driver.find_element_by_name("_save").click()
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Main").click()
        driver.find_element_by_link_text("Sign Out").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpas4879")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_xpath("//div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Add article").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("dtfvghbjnkm")
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("dftgyvbhjnkm")
        #driver.find_element_by_xpath("//form[@action=' /addarticle/added/33/']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Main").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Articles'])[1]/following::h2[1]").click()
        driver.find_element_by_name("text").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("comment")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Sign Out").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpas4879")
        driver.find_element_by_link_text("Main").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Articles'])[1]/following::h2[1]").click()
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testuser")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("testpas4879")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_xpath("//input[@value='Log in']").click()
        driver.find_element_by_xpath("//div[@id='model-user']/a/strong").click()
        driver.find_element_by_link_text("testuser").click()
        driver.find_element_by_link_text("Delete").click()
        driver.find_element_by_xpath("//input[@value=\"Yes, I'm sure\"]").click()
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Sign Out").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()