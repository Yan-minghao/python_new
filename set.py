# s={1,2,4,111,5,10}
#
# s=set([1,2,3,1,1,1])
# s=set(['helll'])
# s=set({'name':'ymh','age': 18})
#
# s={1,2,3,4,6,'a'}
# s1={333}
# print(len(s))
# s1.add(100)
# s.update(s1)
# print(s,type(s))
# print(s.pop())
# s.remove('a')
# print(s,type(s))

#集合运算

ss={1,2,3,5,6}
ss1={0,3,5,6,9}
# 交集
print(ss & ss1)
# 并集
print(ss | ss1)
# 差集
print(ss - ss1)
# 亦或集
print(ss ^ ss1)
