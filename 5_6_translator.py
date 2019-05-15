"""
Автоматизированный поэтический перевод на албанский.

Замена четных гласных:
ключи словаря glasn - гласные, которые заменяются на значения по ключу

Замена глухих согласных:
ключи словаря soglasn - глухие согласные, которые заменяются на значения по ключу (звонкие согласные)
"""
FILENAME = '5_6_data.txt'

glasn = {'а': 'о', 'е': 'и', 'ё': 'ё', 'и': 'е',
         'о': 'а', 'у': 'у', 'ы': 'ы', 'э': 'э',
         'ю': 'йу', 'я': 'и'}
soglasn = {'п': 'б', 'ф': 'в', 'к': 'г', 'т': 'д',
           'с': 'з', 'ш': 'ж'}

with open(FILENAME, 'r', encoding='utf8') as f:
    for stroka in f:
        line = stroka.strip()
        # Первая часть. Замена четных гласных в строке
        for each in line:
            glasn_ind = 0
            if each in glasn.keys():
                glasn_ind += 1
                if glasn_ind % 2 == 0:
                    print(id(line))
                    line_ind = line.index(each)
                    line = line[:line_ind] + glasn[each] + line[line_ind + 1:]
                    print(id(line))
        # Вторая часть. Замена глухих согласных на звонкие
        for char in soglasn.keys():
            if char in line:
                line = line.replace(char, soglasn[char])
        print(line)
