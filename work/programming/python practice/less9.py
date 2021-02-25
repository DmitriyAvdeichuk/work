import math


# def my_range(start, end, step=1):
#     i = start
#     while i < end:
#         yield i  # возвр значение и приостанавливает ход функции
#         i += step
#
#
# for i in my_range(0, 5):
#     print(i)
#
# print(my_range(0, 5))

# lst1 = [math.sin(element) for element in range(0, 20)]
#
# print(lst1)
#
# #
# def sinus(number):
#     i = 0
#     while i < number:
#         yield math.sin(i)
#         i += 1
#
#
# print(sinus(20))

#
def foo(list):
    index = 0
    for element in list:
        yield index, element
        index += 1


lst = [1, 2, 3, 4, 5, 3, 2, 1]

for i, elem in foo(lst):
    print(i, elem)

print(foo(lst))


# def foo(number):
#     i = 0
#     number = str(number)
#     for element in number:
#         i += int(element)
#     return i
#
#
# print(foo(123))
#
# i = '123'
#
#
# print('hello world!')