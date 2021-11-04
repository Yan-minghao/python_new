# 员工管理系统 练习
print('=' * 15, '欢迎使用员工管理系统', '=' * 15)

while True:
    print('请选择要做的操作：')
    print('\t1、查询员工')
    print('\t2、添加员工')
    print('\t3、删除员工')
    print('\t4、退出系统')
    user_choose = int(input('请选择(1-4):'))
    if user_choose == 1:
        pass  # 查询员工
    elif user_choose == 2:
        pass  # 添加员工
    elif user_choose == 3:
        pass  # 删除员工
    elif user_choose == 4:
        print()
        print('退出系统 ', '-' * 4)
        break
    else:
        print('输入有误，请重新输入')
