# 返回值 return fn1 表示对象fn1  fn1() 表示函数
def fn1():
    return


# print(fn1)
# print(fn1())

def sum(*d):
    a = 0
    for i in d:
        a += i
    return a


print(sum(1, 3, 10, -1000))
