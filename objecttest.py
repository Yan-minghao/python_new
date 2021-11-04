# 面向对象

class MyClass():
    pass


my1 = MyClass()
my2 = MyClass()
my3 = MyClass()
# print(my1)
# print(my2)
# print(my3)
# print(isinstance(my1,MyClass))
my3.name = 'hhh'
print(my3.name)


#
# 类方法中必须传一个形参     方法调用时，第一个参数有解析器传入，写类方法至少写一个参数
class Person:
    name = 'swk'

    def say_hello(self):
        print('你好')
        print('你好，我是', self.name)


p = Person()
p.name = 'sdadasdas'
p2 = Person()
p2.name = '11111'
p.say_hello()
p2.say_hello()
