l = ['bb', 'c', 'aaa']

##sort() 排序
# l.sort()
print(l)

# l.sort(key=len)
# print(l)

# sorted 不改变原来对象  不仅仅适用于列表其他的也能用
# sort   改变之前的对象  仅使用于列表
print(sorted(l, key=len))
print(l)
