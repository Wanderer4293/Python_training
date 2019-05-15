from libs.driver import Driver


class WebElement:
    def __init__(self, locator):
        self.driver = Driver()
        self.locator = locator


class Field(WebElement):
    def fill_with(self, data):
        element = self.driver.find_element_by_name(self.locator)
        element.click()
        element.clear()
        element.send_keys(data)
