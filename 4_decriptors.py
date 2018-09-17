"""Пересчет аттрибута Mass.gr при определении аттрибута kg"""
class Kg:
    def __init__(self, value=0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Gr:
    def __get__(self, instance, owner):
            res = instance.kg*1000
            return res

    def __set__(self, instance, value):
        raise AttributeError('Read only attribute')


class Mass:
    kg = Kg()
    gr = Gr()


a = Mass()
a.kg = 100
print(a.kg)
print(a.gr)
