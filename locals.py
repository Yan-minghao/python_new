#命名空间 locals() 函数内部   globals()的全局的
print(locals())
print(type(locals()))
b=200
def fu1():
    a=100
    print(b)
fu1()