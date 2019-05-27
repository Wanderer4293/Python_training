



class GroupHelper:

    def __init__(self,app):
        self.app = app

    def AddGroup(self, parameters):
        driver = self.app.driver
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

    def ModifyGroup(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="content"]/form/span[1]/input').click()
        driver.find_element_by_name("edit").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("1111111")
        driver.find_element_by_name("update").click()
        driver.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()

    def DeleteGroup(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="content"]/form/span[1]/input').click()
        driver.find_element_by_name("delete").click()