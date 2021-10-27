###装饰器 高阶函数 开发时需要遵循OCP原则(开闭原则:Open Closed Principle, OCP))
## OCP原:不修改原函数的情况下，来对程序进行扩展

def add (a,b):
    return a+b

def mut(a,b) :
    return a*b

# 调用add 函数前后分别进行计算输出和

def new_add(a,b):
    print('计算开始')
    num=add(a,b)
    print('计算结束')
    return num

# print(new_add(100,200))

def new_util(fn):
    print('计算开始')
    num= int(fn)
    print('计算结束')
    return num

# print(new_util(mut(1,2)))


def begin_end(old) :
    ##   *args 接收所有位置参数
    ##   **kwargs 接收所有关键字参数
    # *args,**kwargs 装包
    def new_funcation(*args , **kwargs):
        print('begin_end 计算开始')
        # args,kwargs 拆包
        result = old(*args , **kwargs)
        print('begin_end 计算结束')
        return result
    return new_funcation

def fn111():
    print('hhhhhh')
r=begin_end(fn111)

r1= begin_end(add)
print(r1(1000,33333))


print(r())

