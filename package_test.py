## 封装测试     装饰器


class Amail:
    def __init__(self,name):
        self._name=name
        print('父类开始创建%s'%self)
    def run(self):
        print('父类跑了')
    def week(self):
        print('父类走了')

class Dog(Amail):
    def __init__(self,name,age):
        super().__init__(name)
        self._age=age
    def run(self):
        print('子类跑了')
    def do_run(self):
        print('子类跑了')
    def week(self):
        print('zilei')
        print(super)

d=Dog('123','asd')
d.week()


