#定义一个圆的类计算面积和周长
import math
class Circle(object):#定义一个类
    def __init__(self,r):#初始化函数
        self.r=r

    def get_area(self):
        return math.pi*math.pow(self.r,2)#面积
    def get_perimeter(self):
        return 2*math.pi*self.r#周长

if __name__ == '__main__':
    r=int(input('请输入圆的半径:'))
    c=Circle(r)#创建圆的对象将半径传入
    print(f'圆的面积为:{c.get_area()}')
    print(f'圆的周长为:{c.get_perimeter()}')
    print('圆的面积为:{:.2f}'.format(c.get_area()))
    print('圆的周长为:{:.2f}'.format(c.get_perimeter()))