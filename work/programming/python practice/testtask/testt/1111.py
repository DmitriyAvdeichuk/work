lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in range(0,len(lst), 3):
    print('hello {} {} {}'.format(lst[element], lst[element +1], lst[element +2 ]))
