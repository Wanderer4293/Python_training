


class SessionHelper:


    def __init__(self, app):
        self.app = app

    def Logout(self):
        self.app.driver.find_element_by_link_text("Logout").click()

    def Login(self, cred):
        driver = self.app.driver
        driver.get("http://localhost:81/addressbook/index.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(cred.username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(cred.password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()
        return driver