#记录用户登录日志
import  time
def show_info():
    print('输入提示的数字，执行相应操作:0.退出 1.查看登录日志')

#记录日志
def write_loginfo(user_name):
    with open('log.txt','a')as file: #with磁盘管理器不用手动关闭
        s=f'用户名{user_name},登陆时间：{time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')
#读取日志
def read_loginfo():
    with open('log.txt','r')as file:
        while True:
            line=file.readline()
            if line=='':
                break
            else:
                print(line)


if __name__ == '__main__':
#print(time.time())#秒
#print(time.localtime(time.time()))
#print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())))
    username=input('请输入用户名:')
    pwd=input('请输入密码:')
    if 'admin'==username and 'admin'==pwd:
        print('登陆成功')
        write_loginfo(username)#记录日志
        show_info()#提示用户要执行什么操作
        num=int(input('输入操作数字:'))
        while True:
            if num==0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                read_loginfo()#读取日期
                num=int(input('输入操作数字:'))
            else:
                print('您输入的数字有误！！！')
                show_info()
                num=int(input('输入操作数字'))
    else:
        print('对不起，用户名或密码不正确')




