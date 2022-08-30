class Date:
    # 构造函数
    def __init__(self, year, month, day):  # 实例方法
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):  # 实例方法self指向实例new_day
        self.day += 1  # 这句赋值语句相当于给实例的day赋值
        '''如果想要更改类的变量'''
        # Date.day=10

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    '''通过@staticmethod 定义静态方法 该方法参数中没有self 可以将需要的功提取放在类中
        成为静态方法 但是由于在类中 所以调用的时候需要实例化.parse_from_string
        应用场景 一般返回值是True 或者False'''

    @staticmethod
    def parse_from_string(day_str):
        year, month, day = tuple(day_str.split("-"))  # tuple可以拆包
        '''
        不好的地方 使用了硬编码 
        因为return了Date 当类名发生改变 return也需要更改 不然会报错
        为了解决这种问题 python给出了 类方法
        '''
        return Date(int(year), int(month), int(day))

    '''类方法 第一个参数是类本身 一般返回值中需要有类的时候'''

    @classmethod
    def from_str(cls, date_str):
        year, month, day = tuple(day_str.split("-"))  # tuple可以拆包
        '''
        return 中不再是类名称 而是用cls cls指向了类
        '''
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = Date(2022, 8, 30)
    new_day.tomorrow()  # python会自动转换为tomoorrow(new_day)
    print(new_day)
    '''当我想要传递的参数为字符串2022-8-30 但是构造函数是三个参数的值
           这时候就可以用到静态函数'''
    day_str = "2022-08-28"
    # 常规方法用split 在外部处理 这种方式每一次实例化的时候都需要去拆包 不方便
    # year, month, day = tuple(day_str.split("-"))  # tuple可以拆包
    # new_day=Date(int(year),int(month),int(day))
    '''通过调用静态方法 用staticmethod完成初始化'''
    day = Date.parse_from_string(day_str)
    day1 = Date.from_str(day_str)
    print(day)
    print(day1)
