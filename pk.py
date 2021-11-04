aggressivity = 2  # 攻击力
life = 2  # 生命值
print('请选择你的身份：')
print('\t1、唐僧')
print('\t2、白骨精')
num = int(input('请选择(1-2)'))
if num == 1:
    print('你已选择唐僧1,恭喜你将以唐僧身份进行游戏')
elif num == 2:
    print('你虽然')
else:
    print('')

isCard = True
while isCard:
    print('请选择你要的操作：')
    print('         1、练级：')
    print('         2、打Boss')
    print('         3、逃跑')
    print(f"你的身份是唐僧，你的攻击力是:{aggressivity} 你的生命值是: {life}")
    select = int(input('请选择(1-3):'))
    if select == 1:
        aggressivity += 2
        life += 2
    elif select == 2:
        print('开始大boss')
    elif select == 3:
        print('逃跑了')
        isCard = False
        break
