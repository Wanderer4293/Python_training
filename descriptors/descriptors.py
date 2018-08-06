import json


class ConfigHandler:
    _number = None
    _flag = None

    def __init__(self):
        self.config_file = self.open_file()

    @property
    def number(self):
        if not self._number:
            self._number = self.config_file['number'].to_bytes(4, byteorder='big', signed=False)
        return self._number

    @property
    def flag(self):
        if not self._flag:
            self._flag = self.config_file['flag']
        return self._flag

    @staticmethod
    def open_file():
        file_path = 'config.json'
        with open(file_path, 'r', encoding='utf-8') as config_json:
            return json.load(config_json)


class User:
    _binary_id = None

    def __init__(self):
        self.config = ConfigHandler()

    @property
    def binary_id(self):
        if not self._binary_id:
            self._binary_id = config.number
        return self._binary_id

    @binary_id.setter
    def binary_id(self, id):
        if self.config.flag:
            self._binary_id = id.to_bytes(4, byteorder='big', signed=False)
        else:
            raise Exception("Can't assigned because the flag is False. Try switching it to `True`")


person = User()
person.binary_id = 34325
print(person.binary_id)
