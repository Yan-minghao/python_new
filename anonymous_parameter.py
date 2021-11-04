###匿名函数   匿名函数一般都是 filter()  lambda map() 使用简单条件
# filter()
def fu(a, b):
    return a + b


# lambda a,b :a+b)(10,20)
print((lambda a, b: a + b)(10, 20))

# 语法：lambda 参数列表 : 返回值


##map()
l = [1, 2, 3, 4, 5]
r = map(lambda i: i + 1, l)
print(list(r))
