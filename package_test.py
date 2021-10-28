## 封装测试     装饰器


class Amail:
    def __init__(self):
        print('父类开始创建%s'%self)
    def run(self):
        print('父类跑了')
    def week(self):
        print('父类走了')

class Dog(Amail):
    def run(self):
        print('子类跑了')

d=Dog()
d.run()


