#模拟用户登录 最多输入三次
for i in  range(1,4):
    user_name=input('请输入用户名:')
    user_pwd=input('请输入密码')
    if user_name=='admin' and user_pwd=='19951205':
        print('登陆成功')
        break
    else:
        print('用户密码不正确')
        if i<3:
            print(f'您还有{3-i}次输入机会')
else:
    print('对不起，三次输入错误，请联系后台管理员')