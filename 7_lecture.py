import ast
import copy
import itertools

FILENAME = "7_input.txt"


class Words:
    """
    >>> FILENAME = "7_input.txt"
    >>> with open(FILENAME, encoding='utf8') as f:
    ...     data = ast.literal_eval(f.read())
    >>> words_instance = Words(data['words'])
    >>> print(words_instance.words)
    [['съездил', '+-'], ['Вася', '+-'], ['Пете', '+-'], ['по уху', '-+-', '+--']]
    >>> print(words_instance.word(1))
    Вася
    >>> print(words_instance.patterns(1))
    ['+-']
    >>> print(words_instance.word(2))
    Пете
    >>> print(words_instance.patterns(2))
    ['+-']
    >>> print(len(words_instance))
    4
    """
    def __init__(self, data):
        self.words = copy.deepcopy(data)

    def __len__(self):
        return len(self.words)

    def word(self, idx):
        return self.words[idx][0]

    def patterns(self, idx):
        return self.words[idx][1:]


class ElectricPoet:
    """
    >>> FILENAME = "7_input.txt"
    >>> with open(FILENAME, encoding='utf8') as f:
    ...     data = ast.literal_eval(f.read())
    >>> print(ElectricPoet(data).words.word(1))
    Вася
    >>> print(ElectricPoet(data).pattern)
    +-+-+-+--
    >>> print(ElectricPoet(data).verses)
    ... #doctest: +NORMALIZE_WHITESPACE
    ['съездил Вася Пете по уху', 'съездил Пете Вася по уху', 'Вася съездил Пете по уху',
     'Вася Пете съездил по уху', 'Пете съездил Вася по уху', 'Пете Вася съездил по уху']
    >>> print('\\n'.join(ElectricPoet(data).verses))
    съездил Вася Пете по уху
    съездил Пете Вася по уху
    Вася съездил Пете по уху
    Вася Пете съездил по уху
    Пете съездил Вася по уху
    Пете Вася съездил по уху
    """
    def __init__(self, data):
        self.words = Words(data['words'])
        self.pattern = data['pattern']

        vidx = []
        for indices in itertools.permutations(range(len(self.words))):
            pattern_tail = self.pattern
            for i in indices:
                for p in self.words.patterns(i):
                    if pattern_tail.startswith(p):
                        pattern_tail = pattern_tail[len(p):]
                        break
                else:
                    break
            else:
                vidx.append(indices)

        #Последующие пляски исключают не уникальные и обеспечивают порядок,
        #соответствующий порядку нахождения перестановок. В частности, строка
        #с первоначальным порядком слов всегда идёт первой.
        self.verses = set()
        for n, indices in enumerate(vidx):
            self.verses.add((n, ' '.join([self.words.word(i) for i in indices])))
        self.verses = list(self.verses)
        self.verses.sort()
        self.verses = [v for _, v in self.verses]


def main():
    with open(FILENAME, encoding='utf8') as f:
        data = ast.literal_eval(f.read())
    print('\n'.join(ElectricPoet(data).verses))


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod(verbose=1)
