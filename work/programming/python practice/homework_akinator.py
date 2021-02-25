import json

with open('akinatorfile.txt', 'r') as file:
    a = json.load(file)
    print(a)


def play_again():
    while True:
        ask_again = input('Хотите сыграть ещё раз? :')
        if ask_again == '+':
            akinator(a)
        elif ask_again == '-':
            print('Спасибо за игру!')
            return False
        elif ask_again != '+' and ask_again != '-':
            print('Введите + или -')
            continue


def add(somedict):
    adding_key = input('введите вопрос: ')
    adding_value = input('введите ответ: ')
    somedict[adding_key] = adding_value
    with open('akinatorfile.txt', 'w') as file:
        json.dump(somedict, file, indent=4)
    play_again()


def akinator(somedict):


    else:
        play_again()


akinator(a)
