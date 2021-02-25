import sys
import os
import threading


def foo(path):
    a = os.listdir(path)
    for element in a:
        if os.path.isfile(element):
            print(element + ' - файл')

        else:
            print(element + ' - Папка')

#
# # def foo1(path):
# #     a = os.listdir(path)
# #     for element in a:
# #         if os.path.isdir(element):
# #             print(element + '\n' + '\t' + str(os.listdir(element)))
# #             foo(path + '\\' + element)
# #
# #         else:
# #             print(element)
#
#
foo('D:\\python practice')


# def replace(folder1, folder2):
#     # print(os.listdir(folder1))
#     # print(os.listdir(folder2))
#     for element in os.listdir(folder1):
#         os.remove(folder1 + '//' + element)
#         os.rename(folder2 + '//' + element, folder1 + '//' + element)
#
#
# replace('D:\\folder1', 'D:\\folder2')
