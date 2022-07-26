# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  16:25
# 从键盘录入密码，可输入三次
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='666':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1
else:
    print('三次密码输入错误')