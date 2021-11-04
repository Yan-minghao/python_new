###高阶函数
lst = [1, 2, 3, 4, 5, 6, 7]


def function(fun, lst):
    new = []
    for ls in lst:
        if fun:
            new.append(ls)
    return new


# print(function(lst))lst

def fu1(i):
    if i % 2 == 0:
        return True
    return False


print(function(fu1(2), lst))

# 匿名函数
