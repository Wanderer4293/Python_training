# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from Task1.model.Credentials import Credentials
from Task1.model.GroupParameters import GroupParameters
from Task1.model.ContactParameters import ContactParameters
from Task1.fixture.Application import Application
import random
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_untitled_test_case(app):
    app.session.Login(Credentials(Username="admin", Password="secret"))
    app.group.AddGroup(GroupParameters(GroupName=random.randint(1, 1000000),
                                         GroupHeader=random.randint(1, 1000000),
                                         GroupFooter=random.randint(1, 1000000)))
    app.contact.AddContact(ContactParameters())
    app.contact.ModifyContact()
    app.contact.DeleteContact()
    app.group.ModifyGroup()
    app.group.DeleteGroup()
    app.session.Logout()
    time.sleep(5)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()
