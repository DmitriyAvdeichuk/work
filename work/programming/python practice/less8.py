import itertools
import string

with open('voina-i-mir.docx', 'r') as file:
    """чтение файла и подсчёт слов и их количества в тексте. но пока проблема с чтением скачанных книг"""
    text = file.read().replace('\n', '')
    newtext = ''.join(element for element in text if element not in string.punctuation)
    dictcount = {element: newtext.count(element) for element in newtext.split(' ')}

new_d = {}

for k in sorted(dictcount, key=len*value, reverse=True):
    new_d[k] = dictcount[k]
combos = []
d1 = ['!', '#', '%']
for l in range(0, len(d1) + 1):
    """" создал лист со всеми комбинациями значений"""
    for subset in itertools.permutations(d1, l):
        if len(subset) == 3:
            combos.append(''.join(subset))


def dictionary(somedict, somelist, sometxt):
    for element in somelist:
        for key, value in somedict.items():
            if len(key) > 4:
                sometxt = sometxt.replace(key, element)

    return sometxt


print(dictionary(new_d, combos, newtext))
print(new_d)
print(combos)
