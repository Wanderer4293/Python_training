from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Application:

        def __init__(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.verificationErrors = []
            self.accept_next_alert = True

        def Logout(self):
            self.driver.find_element_by_link_text("Logout").click()

        def AddGroup(self, parameters):
            driver = self.driver
            driver.find_element_by_link_text("groups").click()
            driver.find_element_by_name("new").click()
            driver.find_element_by_name("group_name").click()
            driver.find_element_by_name("group_name").clear()
            driver.find_element_by_name("group_name").send_keys(parameters.GroupName)
            driver.find_element_by_name("group_header").click()
            driver.find_element_by_name("group_header").clear()
            driver.find_element_by_name("group_header").send_keys(parameters.GroupName)
            driver.find_element_by_name("group_footer").click()
            driver.find_element_by_name("group_footer").clear()
            driver.find_element_by_name("group_footer").send_keys(parameters.GroupName)
            driver.find_element_by_name("submit").click()
            driver.find_element_by_link_text("group page").click()

        def AddContact(self, contactParameters):
            driver = self.driver
            driver.find_element_by_link_text("add new").click()

            driver.find_element_by_name("firstname").click()
            driver.find_element_by_name("firstname").clear()
            driver.find_element_by_name("firstname").send_keys(contactParameters.FirstName)

            driver.find_element_by_name("middlename").click()
            driver.find_element_by_name("middlename").clear()
            driver.find_element_by_name("middlename").send_keys(contactParameters.MiddleName)

            driver.find_element_by_name("lastname").click()
            driver.find_element_by_name("lastname").clear()
            driver.find_element_by_name("lastname").send_keys(contactParameters.LastName)

            driver.find_element_by_name("nickname").click()
            driver.find_element_by_name("nickname").clear()
            driver.find_element_by_name("nickname").send_keys(contactParameters.NickName)

            driver.find_element_by_name("title").click()
            driver.find_element_by_name("title").clear()
            driver.find_element_by_name("title").send_keys(contactParameters.Title)

            driver.find_element_by_name("company").click()
            driver.find_element_by_name("company").clear()
            driver.find_element_by_name("company").send_keys(contactParameters.Company)

            driver.find_element_by_name("address").click()
            driver.find_element_by_name("address").clear()
            driver.find_element_by_name("address").send_keys(contactParameters.Address)

            driver.find_element_by_name("home").click()
            driver.find_element_by_name("home").clear()
            driver.find_element_by_name("home").send_keys(contactParameters.HomeTelephone)

            driver.find_element_by_name("mobile").click()
            driver.find_element_by_name("mobile").clear()
            driver.find_element_by_name("mobile").send_keys(contactParameters.MobileTelephone)

            driver.find_element_by_name("work").click()
            driver.find_element_by_name("work").clear()
            driver.find_element_by_name("work").send_keys(contactParameters.WorkTelephone)

            driver.find_element_by_name("fax").click()
            driver.find_element_by_name("fax").clear()
            driver.find_element_by_name("fax").send_keys(contactParameters.Fax)

            driver.find_element_by_name("email").click()
            driver.find_element_by_name("email").clear()
            driver.find_element_by_name("email").send_keys(contactParameters.Email)

            driver.find_element_by_name("homepage").click()
            driver.find_element_by_name("homepage").clear()
            driver.find_element_by_name("homepage").send_keys(contactParameters.HomePage)

            Select(driver.find_element_by_name("bday")).select_by_index("5")
            Select(driver.find_element_by_name("bmonth")).select_by_index("10")
            driver.find_element_by_name("byear").click()
            driver.find_element_by_name("byear").clear()
            driver.find_element_by_name("byear").send_keys("1990")

            Select(driver.find_element_by_name("aday")).select_by_index("5")
            Select(driver.find_element_by_name("amonth")).select_by_index("5")
            driver.find_element_by_name("ayear").click()
            driver.find_element_by_name("ayear").clear()
            driver.find_element_by_name("ayear").send_keys("1991")

            driver.find_element_by_name("submit").click()

        def Login(self, cred):
            driver = self.driver
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

        def destroy(self):
            self.driver.quit()