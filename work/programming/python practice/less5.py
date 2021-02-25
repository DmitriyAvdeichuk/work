# class A:
#     def __init__(self):
#         print('A')
#
#
# class B(A):
#     def __init__(self):
#         print('B')
#         super().__init__()
#
#
# class C(A):
#     def __init__(self):
#         print('C')
#         super().__init__()
#
#
# class D(B, C):
#     def __init__(self):
#         print('D')
#         super().__init__()
# d=D()
#
# import inspect
# print(inspect.getmro(D))

# class A:
#     """nu zdarova"""
#
#
# print(A.__doc__)


# class Mine(object):
#
#     def __init__(self):
#         self._x = 'some value'
#
#     @property
#     def prop(self):
#         return self._x
#
#
# mine = Mine()
# mine.prop()  # some value
# mine.prop = 'other value'  # attributeerror
# del mine.prop  # attributeerror


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
#
# d = {i: factorial(i) for i in range(7)}
# print(d)

# l = [elem for elem in range(10)]
# print(l)
#
#
# def func(x):
#     return x + 5
#
#
# l = list(map(lambda x: x + 5, l))
# print(l)
#
# l = list(map(func, l))
# print(l)
#
# l = [1, 2, 3, 4, 5, 10, 15, 20]
#
# l = list(map(lambda x: 0 if x % 5 == 0 else x, l))
# print(l)

# def profit(money, years):
#     i = 1
#     while i <= years:
#         money *= 1.1
#         i += 1
#     return money
#
#
# print(profit(100, 3))
#

# n = int(input())
#
# b = ''
#
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
#
# print(b)


def binar(number):
    b = ''
    while number != 0:
        b = str(number % 2) + b
        number = number // 2
    while len(b) < 8:
        b = '0' + b
    return b


print(binar(2))
