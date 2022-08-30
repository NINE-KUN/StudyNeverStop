'''python有属性 '''
class A():
    '''在aa前面加_ 便成私有属性 无法通过实例。aa访问 子类也没办法访问
           它只能通过类中的公共方法访问'''
    def __init__(self,a):
        self.__aa=a #私有属性
    def b(self):
        return self.__aa+1

if __name__ == '__main__':
    A1=A(1)
    #print(A1.aa) 无法访问
    '''如果想访问私有属性 可以通过以下方法'''
    print(A1._A__aa) #其实私有化就是python把它访问格式变成了(实例化._classnamne__attr)
    print(A1.b())