import os.path
filename='student_txt'
def main():
    while True:
        menm()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定的那个要退出系统么？y/n')
                if answer=='y'or answer=='Y':
                    print('谢谢您的使用！')
                    break #退出系统
                else:
                    continue #继续
            elif choice==1:
                insert() #录入学生信息
            elif choice==2:
                search() #查找学生信息
            elif choice==3:
                delete() #删除学生信息
            elif choice == 4:
                modify() #修改学生信息
            elif choice ==5:
                sort() #排序
            elif choice ==6:
                total() #统计学生总人数
            elif choice==7:
                show() #显示所有学生信息
def menm():
    print('================================学生信息管理系统================================')
    print('---------------------------------功能菜单-------------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')

def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if not id: #如果为空退出循环
            break
        name=input('请输入姓名:')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            java = int(input('请输入java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #将录入的学生信息保存到字典当中
        student= {'id':id,'name':name,'english':english,'python':python,'java':java}
        #将学生信息添加到列表当中
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y'or answer=='Y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8') #如果存在以追加的方式打开
    except:
        stu_txt=open(filename,'w',encoding='utf-8') #如果不存在以写入的方式打开
    for item in lst: #遍历lst 写入stu_txt
        stu_txt.write(str(item)+'\n')#将列表转换为字符串类型
        stu_txt.close()

def search():
    student_query=[]#定义列表
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2')
            if mode=='1':
                id=input('请输入学生ID')
            elif mode=='2':
                name=input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
        #显示查询结果
        show_student(student_query)
        #清空列表
        student_query.clear()
        answer=input('是否继续查询？y/n\n')
        if answer=='y'or answer=='Y':
            continue
        else:
            break
    else:
        print('暂未保存学生信息')
        return
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    #定义标题显示格式
    formatter_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(formatter_title.format('ID','姓名','英语成绩','paython成绩','java成绩','总成绩'))
    #定义内容显示格式
    formatter_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(formatter_data.format(item.get('id'),
                                    item.get('name'),
                                    item.get('english'),
                                    item.get('python'),
                                    item.get('java'),
                                    int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                    ))
def delete():
    while True:
        student_id=input('请输入要删除的ID(如1001):')
        if student_id != '': #如果删除的学生信息ID不为空
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file: #运用os模块打开文件
                    student_old=file.readlines() #读取所有数据放入列表
            else:
                student_old=[] #文件不存在列表为空
                flag=False #标记未删除
            if student_old: #判断列表
                with open(filename,'w',encoding='utf-8')as wfile:#以只写的方式打开文件
                    d={}
                    for item in student_old: #遍历列表
                        d=dict(eval((item)))#将字符串转换成字典
                        if d['id']!=student_id:#字典中的ID和删除的学生ID不相等就将这条信息写入文件
                            wfile.write(str(d)+'\n') #先将该信息写入
                        else:
                            flag=True #标记已删除
                            if flag:
                                print(f'id为{student_id}的学生信息已被删除')
                            else:
                                print(f'没有找到ID为{student_id}的学生信息')
        else:
            print('无学生信息')
            break
            show() #删除之后要重新显示所有学生信息
            answer=input('是否继续删除？y/n\n')
            if answer=='y'or answer=='Y':
                continue
            else:
                break



def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:#通过只读的方式打开文本
            student_old=rfile.readlines() #将文本中的内容赋值给变量
    else:
        return
    student_id=input('请输入要修改的学生ID')
    with open(filename,'w',encoding='utf-8') as wfile:#通过只写的方式打开文本
        for item in student_old:#遍历
            d=dict(eval(item))#创建字典
            if d['id']==student_id:
                print('找到学生信息，请进行修改')
                while True:
                    try:
                        d['name']=input('请输入姓名')
                        d['english']=input('请输入英语成绩')
                        d['python']=input('请输入python成绩')
                        d['java']=input('请输入java成绩')
                    except:
                        print('您的输入有误请重新输入')
                    else:
                      break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他学生信息？y/n\n')
        if answer=='y'or answer=='Y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_lst=rfile.readlines()
            student_new=[]
            for item in student_lst:
                d=dict(eval(item))
                student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择(0.升序 1.降序):')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序)')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool) #key(排序关键字)
    elif mode=='2':
        student_new.sort(key=lambda x:int(x['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x:int(x['java']),reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)
def total():
        if os.path.exists(filename):#判断文件是否存在
            with open(filename,'r',encoding='utf-8') as rfile:#读取文件
                student=rfile.readlines()#读取全部内容
                if student:
                    print(f'一共有{len(student)}名学生')
                else:
                    print('还没有录入学生信息')
        else:
            print('暂未保存数据信息...')

def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student=rfile.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存数据信息...')
if __name__ == '__main__':
    main()