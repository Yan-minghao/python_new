#闭包


def fn1():
    def fn3():
        print('hhhhh')
    return fn3()
fn1()