# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from group import Group
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class GroupTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
    
    def create_group(self, driver, group):
        # open groups page
        driver.find_element_by_link_text("groups").click()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill group firm
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()

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

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, user_name="admin", password="secret")
        self.create_group(driver, Group(name="aaa", header="aaa", footer="aaa"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, user_name="admin", password="secret")
        self.create_group(driver, Group(name="", header="", footer=""))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
