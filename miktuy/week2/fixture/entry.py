from libs.page_elements import Field


class EntryHelper:
    def __init__(self, app):
        self.app = app

    def create(self, entry):
        driver = self.app.driver
        # open add new page
        driver.find_element_by_link_text("add new").click()
        # fill new entry firm
        Field(driver, 'firstname').fill_with(entry.firstname)
        Field(driver, 'nickname').fill_with(entry.nickname)
        Field(driver, 'middlename').fill_with(entry.middlename)
        Field(driver, 'email').fill_with(entry.email)
        # submit entry creation
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def delete_first_entry(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        driver.switch_to.alert.accept()
