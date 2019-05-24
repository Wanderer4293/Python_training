from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Task1.fixture.Session import SessionHelper
from Task1.fixture.Group import GroupHelper
from Task1.fixture.Contact import ContactHelper


class Application:

        def __init__(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.verificationErrors = []
            self.accept_next_alert = True
            self.session = SessionHelper(self)
            self.group = GroupHelper(self)
            self.contact = ContactHelper(self)

        def destroy(self):
            self.driver.quit()