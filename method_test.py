##### method

class Person:
    def test(self):
        print('实例方法，输出了')
    @classmethod
    def class_test(cla):
        print('类方法，输出了')
    @staticmethod
    def static_test():
        print('静态方法，输出了')

if __name__ == '__main__':
    p=Person()
    p.test()
    p.class_test()
    p.static_test()