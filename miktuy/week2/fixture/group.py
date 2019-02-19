from libs.page_elements import Field


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill group firm
        Field(driver, 'group_name').fill_with(group.name)
        Field(driver, 'group_header').fill_with(group.header)
        Field(driver, 'group_footer').fill_with(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()
