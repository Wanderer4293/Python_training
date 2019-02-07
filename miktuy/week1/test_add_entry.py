# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from entry import Entry
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver, user_name, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user_name)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_entry(self, driver, entry):
        # open add new page
        driver.find_element_by_link_text("add new").click()
        # fill new entry firm
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(entry.firstname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(entry.nickname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(entry.middlename)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(entry.email)
        # submit entry creation
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, user_name="admin", password="secret")
        self.create_entry(driver, Entry(firstname="Test",
                                        nickname="NS",
                                        middlename="FOS",
                                        email="test.fos@mail.mu"))
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
