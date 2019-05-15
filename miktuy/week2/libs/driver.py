from selenium.webdriver.chrome.webdriver import WebDriver


class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Driver(metaclass=Singleton):
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)

    def __getattr__(self, item):
        return getattr(self.driver, item)
