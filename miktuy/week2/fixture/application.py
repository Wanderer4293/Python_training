#from selenium.webdriver.chrome.webdriver import WebDriver
from libs.driver import Driver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.entry import EntryHelper


class Application:
    def __init__(self):
        # self.driver = WebDriver()
        self.driver = Driver()
        # self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.entry = EntryHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
