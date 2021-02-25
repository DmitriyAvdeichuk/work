import string
import itertools


def rewrite(somedict, sometext):
    combos = []
    d1 = ['!', '#', '%']
    for l in range(0, len(d1) + 1):
        """" создал лист со всеми комбинациями значений"""
        for subset in itertools.permutations(d1, l):
            if len(subset) == 3:
                combos.append(''.join(subset))
    for element in combos:
        for key in somedict.keys():
            sometext.replace(element, key)
            break
    return sometext


def makedict(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        readed_file = file.read()
        readed_file = readed_file.replace('\n', '')
    newtext = ''.join(element for element in readed_file if element not in string.punctuation)
    dict_with_words = {element: newtext.count(element) for element in newtext.split(' ')}
    accepted_words = {}
    for key, value in dict_with_words.items():
        if value * len(key) > value * 3 + (1 + len(key)):
            accepted_words[key] = value
    sorted_dict = {k: v for k, v in sorted(accepted_words.items(), key=lambda item: item[1], reverse=True)}
    # for element in sorted(accepted_words, key=len):
    #     sorted_dict[element] = accepted_words[element]
    rewrite(accepted_words, newtext)


print(makedict('book.txt'))
