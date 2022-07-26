#使用面向对象的思想，设计自定义类，描述出租车和家用车信息
#封装继承多态
class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no
    def start(self):
        pass
    def stop(self):
        pass
class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)#调用父类init函数
        self.company=company
    def start(self):#重写start方法
        print('乘客您好')
        print(f'我是{self.company}出租车公司的，我的车牌是{self.no},请问您要去哪里')
    def stop(self):
        print('目的地到了，请您付款下车，欢迎再次乘坐')

class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name=name
    def start(self):
        print(f'我是{self.name},我的汽车我做主')
    def stop(self):
        print('目的地到了我们去玩吧')

if __name__ == '__main__':
    taxi=Taxi('上海大众','川A65986','长城')
    taxi.start()
    taxi.stop()
    print('-'*30)
    familycar=FamilyCar('保时捷911','川A951205','钱坤')
    familycar.start()
    familycar.stop()
