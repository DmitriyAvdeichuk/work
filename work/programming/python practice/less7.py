# def foo(stroka):
#     return stroka[:len(stroka) // 2], stroka [len(stroka) // 2:]
#
#
# print(foo('privettpoka'))


# def foo(stroka):
#     return stroka[len(stroka)//4:len(stroka)-len(stroka)//4]
#
#
# print(foo('1234'))

# l = [1, 2, 3]
# i = 0
# try:
#     while True:
#         print(l[i])
#         i += 1
# except IndexError:
#     print('i reached a bound')


# def foo(l):
#     for i, elem in enumerate(l):
#         print(i + elem)
#
#
# l = ['11', '22', '33']
# try:
#     foo(l)
# except TypeError:
#     l=[int(elem)for elem in l]
#     # foo(l)
#
# l.append('44')
# print(l)

# def foo(num1, num2):
#     return num1 / num2
# print(foo(3,4))
# try:
#     print(foo(2,0))
# except ZeroDivisionError:
#     print('wrongnumber')


# class WrongValError(Exception):
#     pass
#
#
# def foo(val):
#     if val != '!!!':
#         raise WrongValError
#     else:
#         print('fine')
#
#
# foo('!!!')
# try:
#     foo(1)
# except WrongValError:
#     print('WRONG!!!')

#
# MyClass = type('MyClass', (), {'number': 0, "string": 'some_str'})
# obj = MyClass()
# print(obj.number)
# print(obj.string)
#
# print(MyClass.__name__)
#
# s = ''
# print(s.__class__)
# print(s.__class__.__class__)
#

def binsearch(lst, number):
    half1 = lst[:len(lst) // 2]
    half2 = lst[len(lst) // 2:]
    if 


binsearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
