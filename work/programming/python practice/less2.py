# # pervaya
# def foo(choto):
#     lst = []
#     for i in str(choto):
#         lst.append(int(i))
#     lst = tuple(lst)
#     print(lst)
#     return lst
#
#
#
#
# foo(123123432573444)

# def foo(lst):
#     odin=1
#     for i in lst:
#         odin *=i
#     print (i)
#     return i
# foo([1,2,3,4,5])


# vtoraya
# def foo(list):
#     p = 1
#     for i in list:
#         p *= i
#     return p
#
#
# def func(list1):
#     sal = foo(list1)
#
#     return [sal // e for e in list1]
#
#
# print(func([1, 2, 3, 4, 5]))

# tretaya
# def count(str):
#     new={i:str.count(i) for i in str}
#     return new
#
# print(count('hello python'))

# class B:
#     n = 5
#
#     def adder(self,v):
#         return v + self.n
# l=B()
# m=B()
# l.n=10
# print(l.adder(3))
# print(m.adder(4))
#
# l.test='hi'
# l.test


# class User:
#     def setName(self, n):
#         self.name = n
#     def getName(self):
#         try:
#             return self.name
#         except:
#             print('no name')
# first= User()
# second=User()
# first.setName('bob')
# print(first.getName())
# second.getName()


# class person:
#     def __init__(self, f, s, q=1):
#         self.firstname = f
#
#         self.secondname = s
#
#         self.qual = q
#
#     def __del__(self):
#         print('До свидания, мистер ', self.firstname, self.secondname)
#
#     def info(self):
#         return '{},{},{}'.format(self.firstname, self.secondname, self.qual)
#
#
# #
# worker = person('s', 'ahahhahaha', 4)
# helper = person('vlad', 'soset', 5)
# weak = person('jeka', 'lisiy', 1)

# vse = [person('dimka', 'nevedimka', 3),
#        person('vladik', 'loh', 2),
#        person('jeka', 'lisiy', 1)]
# for i in vse:
#     print(person.info)

# vse.sort(key=lambda ,p:p.qual, reverse=True)


# print(vse)


class bardi:
    def __init__(self, nickname, profa, lvl=85):
        self.nickname = nickname
        self.profa = profa
        self.lvl = lvl

    def __del__(self):
        print('Никнейм:', self.nickname, ' Профессия:', self.profa, 'Уровень:', self.lvl)

    def info(self):
        return '{} {} {}'.format(self.nickname, self.profa, self.lvl)


bd = bardi('ifasa', 'Bladedancer')
sws = bardi('Sickmind', 'Swordsinger', 72)
# # bd=bardi()
# # bd.profession('sick', 'Bladedancer',85)
# # sws=bardi()
# # sws.profession('Sickmind','Swordsinger', 72)
#
# # print(bd.lvl,sws.nickname)