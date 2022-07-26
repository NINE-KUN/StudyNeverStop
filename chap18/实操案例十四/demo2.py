#推算几天后的日期
import datetime
def inputdate():
    indate=input('请输入开始日期：(20200808)后按回车:')
    indate=indate.strip()
    datestr=indate[0:4]+'-'+indate[4:6]+'-'+indate[6:]
    return  datetime.datetime.strptime(datestr,'%Y-%m-%d')
if __name__ == '__main__':
    print('----------------------推算几天后的日期----------------------------------')
    sddate=inputdate()
    in_num=int(input('请输入间隔天数:'))
    fddate=sddate+datetime.timedelta(days=in_num)
    print('您推算的日期是：'+str(fddate).split('')[0])