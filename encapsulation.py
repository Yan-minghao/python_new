# 封装 类型java  提供get set 方法
# 封装方式 1.隐藏属性名（属性修改一个外部不知道名称）  2.添加get set 方法


class Dog:
    def __init__(self, name, age, gender, height):
        self._name = name
        self._age = age
        self._gender = gender
        self._height = height
        # print('初始化基本信息完成')

    def run(self):
        pass
        # print('开始跑了%s',self.hide_age,self.hide_age,self.hide_gender,self.hide_height)

    # def get_name(self):
    #     return self.hide_name
    # def set_name(self,name):
    #     self.hide_name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


d = Dog('旺财', 1, '男', '25cm')
print(d.name)
d.name = 'sadasd'
print(d.name)
