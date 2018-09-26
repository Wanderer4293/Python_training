""" Пересчет аттрибутов Mass.gr и Mass.tn при определении аттрибута Mass.kg
В дескрипторах Gr и Ton перегружены методы get, set для пересчета кг в граммы и тонны."""


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


class Ton:
    def __get__(self, instance, owner):
            res = instance.kg*0.001
            return res

    def __set__(self, instance, value):
        raise AttributeError('Read only attribute')


class Mass:
    """
    >>> a = Mass()
    >>> a.kg = 100
    >>> b = Mass()
    >>> b.gr = 1
    Traceback (most recent call last):
    ...
    AttributeError: Read only attribute
    >>> c = Mass()
    >>> c.tn = 1
    Traceback (most recent call last):
    ...
    AttributeError: Read only attribute
    >>> print('Масса в кг =', a.kg)
    Масса в кг = 100.0
    >>> print('Масса в кг =', a.gr)
    Масса в кг = 100000.0
    >>> print('Масса в тоннах =', a.tn)
    Масса в тоннах = 0.1
    """
    kg = Kg()
    gr = Gr()
    tn = Ton()


a = Mass()
a. kg = 100

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=1)
