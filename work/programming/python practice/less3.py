# класс-объект создающий другие объекты


# class B:
#     def foo(self):
#         return self
#
#
# b = B()
# print(b is b.foo())
# a = 'stroka'


# class vozv:
#     def __init__(self, stroka):
#         self.stroka = stroka
#
#     def reverse(self):
#         lst = self.stroka.split()
#         lst = lst[::-1]
#         print(lst)
#         stroka1 = ' '.join(lst)
#         print(stroka1)
#         return
#
#
# a = vozv('zdarova ky  maloi')
# vozv.reverse(a)


class shape:
    def __init__(self, izmer):
        self.izmer = izmer

    def sqrt(self):
        pass


class kvadrat(shape):
    def sqr(self):
        return self.izmer ** 2


class treug(shape):
    def __init__(self, storona, a):
        super().__init__(storona)
        self.a = a

    def sqr(self):
        return self.izmer * self.a * 0.5


class krug(shape):
    def __init(self, izmer):
        self.izmer = izmer

    def sqr(self):
        return self.izmer * 3.14


value = shape(4)
triangle = treug(4, 5)
kvadrat1 = kvadrat(value)
circle = krug(5)
print(triangle.sqr(), circle.sqr())
