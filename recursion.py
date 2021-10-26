#递归
def fun1(n):
    if n==1:
        return 1
    return n*fun1(n-1)

# print(fun1(100))

#练习 创建一个函数power 来为任意数字做幂运算 n**i

def power(n,i):
    if i==0:
        return 1
    return n*power(n,i-1)
# print(power(2,10))


#练习2 创建一个函数 ，用来检查一个任意的字符串，是否回文字字符串，如果是返回true 如果不是返回false
# 回文字符串  abcba  字符串从前往后和从后往前是一样的

def isHui(st):
    '''
    用来检查一个任意的字符串，是否回文字字符串，如果是返回true 如果不是返回false
    :param st:
    :return:
    '''
    if len(st)<2 :
        return True
    if st[0]!=st[-1]:
        #使用切面 取第二和倒数第二个中所有的
        return False
    return isHui(st[1:-1])
print(isHui('qwe'))
