import json


class ConfigHandler:

    def __init__(self, file_name):
        with open(file_name, 'r') as cf:
            config_file = json.load(cf)

        self.flag = config_file['flag']


class User:

    def __init__(self, file_name):
        self.config = ConfigHandler(file_name)
        self._id_bytes = None

    @property
    def id_bytes(self):
        print(10 * '*' + 'Return id in bytes!' + 10 * '*')
        return self._id_bytes

    @property
    def id_int(self):
        print(10 * '*' + 'Return id like int!' + 10 * '*')
        return int.from_bytes(self._id_bytes, byteorder='big')

    @id_bytes.setter
    def id_bytes(self, id):
        if self.config.flag:
            self._id_bytes = id.to_bytes(4, byteorder='big', signed=False)
        else:
            raise Exception("Can't assigned because the flag is False. Try to switch it to `True`")


if __name__ == '__main__':
    person = User('config.json')
    person.id_bytes = 100
    print(person.id_bytes)
    print(person.id_int)