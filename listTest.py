# 列表 序列
# 可变序列 list
# 不可变序列
#         字符串 str
#         元组 tuple
# my_list =[10,1111111] #创建空列表
# print(my_list,type(my_list))
# # print(my_list[3])
# print(len(my_list))
# 切片
# testhhh=['1','2','3','4']
# print(testhhh[-1])
# print(testhhh[::-1])
# 列表通用操作 in not in 检查是否存在  len  min  max
# s.index() s.count()
my_list = ['肖战', '李易峰', '张艺兴', 'java']
# print( '肖战1'  not in  my_list )
# print(len(my_list))
# print(my_list.index('李易峰',2,4))

str = 'hello'
my_ = list(str)
my_[2:4] = 'tt'
print(''.join(my_))
