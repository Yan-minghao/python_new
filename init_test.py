class Person:
    def __init__(self, name):
        self.name = name
        print('初始化%s' % self.name)

    def say_hello(self):
        print('大家好，我是：%s' % self.name)


p = Person('郭德纲')
p.say_hello()


class Dog:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        print('初始化基本信息完成')

    def run(self):
        print('开始跑了%s', self.name, self.age, self.height, self.gender)


d = Dog('旺财', 1, '男', '25cm')
d.run()
