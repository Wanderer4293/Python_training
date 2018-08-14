import abc


class Button(abc.ABC):
    def __init__(self):
        self.color = None

    @abc.abstractmethod
    def paint(self, color):
        self.color = color
        print("Now button is {}".format(color))


class CheckBox(abc.ABC):
    def __init__(self):
        self.color = None

    @abc.abstractmethod
    def paint(self, color):
        self.color = color
        print("Now checkbox is {}".format(color))


class WinButton(Button):
    def paint(self, color):
        super().paint(color)


class MacButton(Button):
    def paint(self, color):
        super().paint(color)


class WinCheckBox(CheckBox):
    def paint(self, color):
        super(WinCheckBox, self).paint(color)


class MacCheckBox(CheckBox):
    def paint(self, color):
        super(MacCheckBox, self).paint(color)


class GUIFactory(abc.ABC):

    def __init__(self):
        self.button = None
        self.checkbox = None

    @abc.abstractmethod
    def create_button(self):
        pass

    @abc.abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):
    def create_button(self):
        super().create_button()
        return WinButton()

    def create_checkbox(self):
        super().create_checkbox()
        return WinCheckBox()


class MacFactory(GUIFactory):
    def create_button(self):
        super().create_button()
        return MacButton()

    def create_checkbox(self):
        super().create_checkbox()
        return MacCheckBox()


class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = self.factory.create_button()


if __name__ == '__main__':
    app = Application(MacFactory())
    app.button.paint('Black')


