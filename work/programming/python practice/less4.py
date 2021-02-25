# file = open('some', 'r')
#
# for line in file.readlines():
#     print(line)
#
# file.close()
#
#
#
# with open('some','r') as file:   #в конце само закрывает файл
#     for line in file.readlines():
#         print(line)

#
# with open('some_new','w') as file:
#     file.write('hello python')

# with open('zadachka2', 'w')as file:
#     file.write('privet\n')
#     file.write('poka\n')
#     file.write('zxc\n')
#     file.write('ashkdgsalkjd\n')
# file1 = open('zadachka2', 'r')


# def max_len(file):
#     with open(file, 'r')as file:
#         read = file.read()
#     splitted = read.split()
#     new = ''
#     for word in splitted:
#         if len(word) > len(new):
#             new=word
#     return new
#
# print(max_len('zadachka2'))

# написать модуль, в котором нужно определить функцию , которая принимает файл и вохвоащает словарь символов

# def foo(filepath):
#     with open(filepath, 'r')as file:
#         read = file.read()
#     dict1 = {i: read.count(i) for i in read}
#     return dict1
#
# print(foo('zadachka2'))

# def foo(filepath):
#     with open(filepath, 'r') as file:
#         read = file.read()
#     words = read.split()
#     dict1 = {i: words.count(i) for i in words}
#     return dict1
#
#
# print(foo('zadachka2'))

# def readlines_from_file(filepath):
#     with open(filepath, 'r')as file:
#         lines_from_file = [line.replace('\n', '') for line in file.readlines()]
#     return lines_from_file
#
#
# #
# #
# def foo(filepath1, filepath2):
#     lines_from_file1 = readlines_from_file(filepath1)
#     lines_from_file2 = readlines_from_file(filepath2)
#     d = {}
#     for line1, line2 in zip(lines_from_file1, lines_from_file2):
#         d[line1] = line2
#     return d
#
#
# print(foo('zadachka1', 'zadachka2'))

# def write(filepath, lst):
#     with open(filepath, 'w')as file:
#         for element in lst:
#             file.write(str(element)+ '\n')
#     return lst
#
#
# lst=['privet','andrey','nu kak ti tam']
# write('zadachka2',lst)
#
#

# def stroki(filename, lst):
#     with open(filename, 'w') as file:
#         for element in lst:
#             file.write(str(element)+'\n')
#     return lst
#
#
# # list1 = ['nu','ladno']
#
# stroki('zadachka2', ['privet', 'poka'])
