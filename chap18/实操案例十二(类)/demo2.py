#定义学生类录入5个学生信息存储到列表中
class Student(object):
    def __init__(self,stu_name,stu_age,stu_gender,stu_score):
        self.stu_name=stu_name #属性赋值
        self.stu_age=stu_age
        self.stu_gender=stu_gender
        self.stu_score=stu_score

    def show(self):
        print(self.stu_name,self.stu_age,self.stu_gender,self.stu_score)
if __name__ == '__main__':
    print('请输入五位学员的信息:(姓名#年龄#性别#成绩)')
    lst=[]
    for i in range(0,5):
        s=input(f'请输入第{i+1}位学院的信息和成绩:')
        s_lst=s.split('#')#对字符串进行(split)分割
        #创建学生对象
        stu=Student(s_lst[0],int(s_lst[1]),s_lst[2],float(s_lst[3]))
        lst.append(stu)
    #遍历列表
    for item in lst:#item是个对象
        item.show()
