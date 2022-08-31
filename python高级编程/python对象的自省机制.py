'''魔法函数以及类方法 类调用类方法的练习'''


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}-{month}-{day}".format(year=self.year, month=self.month, day=self.day)

    @classmethod
    def date_str(cls, to_str):
        year, month, day = tuple(to_str.split("-"))
        return cls(int(year), int(month), int(day))


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2022 - self.__birthday.year


if __name__ == '__main__':
    print(Date.date_str('1995-12-5'))
    user = User(Date.date_str('1995-12-5'))
    print(user.get_age())

    '''
    python的自省
    通过一定的机制 查询到对象的内部结构
    '''


class Person():
    name = '钱坤'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student('天津理工大学')
    '''通过__dict__查询属性'''
    '''修改类的属性'''
    user.__dict__["school_address"] = "天津"
    print(user.__dict__)#user是Student的实例 所以__dict__只显示类的参数
    print(Person.__dict__)#因为Person是类 所以字典会很丰富 可以访问到字典的属性
    print(user.name) #name是Person的属性 不是实例user的 所以不是字典类型

    '''dir()函数会列出对象所有属性 比__dict__更强大'''
    print(dir(user))