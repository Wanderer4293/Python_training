import abc


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, message: str) -> None:
        pass


class Observable(abc.ABC):
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print("{} has been removed from subscribed users".format(observer))

    def notify(self, data: str) -> None:
        for observer in self._observers:
            observer.update(data)


class Application(Observable):

    def send_notification(self, notification: str) -> None:
        self.notify(notification)


class User(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return self.name

    def update(self, message: str) -> None:
        super().update(message)
        print("{} receive a new message: {}".format(self.name, message))


if __name__ == '__main__':
    editor = Application()
    user1 = User('username1')
    user2 = User('username2')
    editor.subscribe(user1)
    editor.subscribe(user2)
    editor.send_notification("Hello world!")
    editor.unsubscribe(user1)
    print(30 * '-')
    editor.send_notification("Another message!")
