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
fn4(**h)
# fu2(**)