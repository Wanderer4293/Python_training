class WebElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator


class Field(WebElement):
    def fill_with(self, data):
        element = self.driver.find_element_by_name(self.locator)
        element.click()
        element.clear()
        element.send_keys(data)
