'''魔法函数'''
class Company(object):
    def __init__(self,employee_list):
        self.employee=employee_list

    def __getitem__(self, item):#定义了__getitem__就可以直接遍历实例company
        return self.employee[item]

company=Company(['tom','gary','jerry','lisa'])

employee=company.employee
for item in employee:
    print(item)
print('--------------------------')
'''以上11-13代码等同于以下 因为定义了__getitem__
   将class类型的Company 变成了 可迭代类型 (首先去找有没有__iter__方法 没有就去找__getitem__)
   所以python解释器会去调用__getitem__直到抛出异常循环结束'''
for res in company:
    print(res)
