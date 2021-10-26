# def hello() :
#     print('hello')
#     print('你好')
#     print('再见')
# hello()
#
# def sum(i,j) :
#     return i+j
# print(sum(1,3))
#
# def mut(i,j,k):
#     return i*j*k
#
# print(mut(2,2,4))

# def helloPrint(str):
#     return (f'欢迎{str}登录')
# print(helloPrint('yanminghao'))

# 可变形参 *只能保存位置形参
# def sumNum(*a):
#     sum=0
#     for i in a :
#         sum+=i
#     return sum
# print(sumNum(1,2,3,4,5))
# # 可变形参 **可以接受关键字参数
# def sumNum(**a):
#     print('a',a)
#
# sumNum(a=1)

# 装包   & 解包

# () [] 序列和元组 用*
def fu2(a,b,c) :
    print(a)
    print(b)
    print(c)
# hh = [1,2,3]
# hh = (1,2,3)
# fu1(*hh)
####   字典解包 必须用**
def fn4(a,b,c):
    print(a)
    print(b)
    print(c)
h= {'a':100,'b':200,'c':123 }
# fn4(**h)
# fu2(**)

# help() python 中内置函数  help(obj)
# 文档字符串 doc str
# DocStrings 文档字符串使用惯例：它的首行简述函数功能，第二行空行，第三行为函数的具体描述。
def fu5(a:int,b:str='100')->int :
    '''这是一个helloword 文档字符串

    hhhhhhhh
    '''

    return 10
print(fu5.__doc__)
help(fu5(1))

def printMax(x, y):
    '''打印两个数中的最大值。

    两个值必须都是在整形数。'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, '最大')
    else:
        print(y, '最大')


printMax(3, 5)
print(printMax.__doc__)  # 调用 doc


###高阶函数

