# height = int( input('请输入您的身高cm： ') )
# money  = float( input('请输入您的财富w： '))
# isbuty = int ( input('请输入您的帅值：'))
#
#
# if height>180 and money>1000 and isbuty>500 :
#     print('我一定要嫁给他')
# elif height>180 or money>1000 or isbuty>500 :
#     print('嫁吧，必上不足，比下有余')
# else :
#     print('不嫁')
# a = 0
# num= 0
# while  a <=100 :
#      if a%2 ==1 :
#          num+= a
#          print('奇数值： ',a)
#      a+=1
# print(num)

# a = 0  #数值
# sum = 0 # 求和
# num = 0 # 7的倍数
#
# while a <= 100 :
#     if a %7 ==0 :
#         sum += a
#         num += 1
#         print( a)
#     a+=1
# print(sum)
# print(num)

##练习4  获取用户输入的任意数，判断是否是质数
# number =int ( input('请输入任意整数:'))
# isFlag = False
# num =1
# while num<number  :
#     if number% num ==0:
#        isFlag= True
#     num+=1
# if isFlag :
#     print(number,'不是质数')
# else : print(number,'是质数')



# 获取100 ~ 999 数值
# 获取每个数 个 十 百 数值
# 求和和为某个数值
# a= 100
#
# while a <= 999 :
#     bit= a //100
#     ten =a //10 %10
#     hundredth= a%10
#     # print('a 的数值为： ',a);
#     # print('bit 的数值为： ',bit);
#     # print('ten 的数值为： ',ten);
#     # print('hundredth 的数值为： ',hundredth);
#     if (a== (bit**3)+ (ten ** 3) + (hundredth ** 3)) :
#         print('水仙花数：',a)
#     a+=1
# i=0
# while i< 5 :
#     j=0
#     while j< 10 :
#         print("*",end='')
#         j+=1
#     print()
#     i+=1

# *
# **
# ***
# ****
# *****

# i = 0
# while i < 5:
#     # 创建一个内层循环来控制图形的宽度
#     j = 0
#     while j < i+1:
#         print("*",end='')
#         j += 1
#     print()
#     i += 1


# ****
# ***
# **
# *
# i = 5
# while i >0:
#     # 创建一个内层循环来控制图形的宽度
#     j = 0
#     while j < i-1:
#         print("*",end='')
#         j += 1
#     print()
#     i -= 1

### 九九乘法表
# i = 1;
# while i<=9 :
#     j = 1
#     while j<= i :
#          print(f"{j}*{i}={i*j}",end=' ')
#          j+=1
#     print()
#     i += 1

# a= 1
# while a<=100 :
#     isFlag = True
#     num = 2
#     while num < a:
#         if a % num == 0:
#             isFlag = False
#         num += 1
#     if isFlag:
#         print(a, '是质数')
#
#     a+=1
# from time import time
#
# be=time()
# a= 1
# while a<=100000 :
#     isFlag = True
#     num = 2
#     while num < a ** 0.5:
#         if a % num == 0:
#             isFlag = False
#             break
#         num += 1
#     if isFlag:pass
#         # print(a, '是质数')
#     a+=1
# end=time()
# print(end-be)
