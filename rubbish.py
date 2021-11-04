### 垃圾回收
class Person:
    ###对象被删除方法
    def __del__(self):
        print('对象已删除%s'%self)

p=Person()
# p=None
input('请输入文字')



