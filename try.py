###

class MyError(Exception):
    pass

try:
    print(10/0)
except:
    raise MyError()
else:
    print('未见异常')

