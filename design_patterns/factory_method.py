import abc


class Button(abc.ABC):

    def __init__(self):
        self.color = None

    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def on_click(self):
        pass


class WindowsButton(Button):
    def render(self):
        super().render()
        print("render Windows button")

    def on_click(self):
        super().on_click()
        print("You pressed the the Windows button")


class HTMLButton(Button):
    def render(self):
        super(HTMLButton, self).render()
        print("render HTML button")

    def on_click(self):
        super(HTMLButton, self).on_click()
        print("You pressed the HTML button")


class Application:

    def __init__(self, platform):
        self.platform = platform
        self.button = self.identify_button()

    def identify_button(self):
        if self.platform == 'Web':
            return HTMLButton()
        elif self.platform == 'Windows':
            return WindowsButton()


if __name__ == '__main__':
    web_app = Application('Web')
    web_app.button.render()
    web_app.button.on_click()
    print(30 * '_')
    win_app = Application('Windows')
    win_app.button.render()
    win_app.button.on_click()

