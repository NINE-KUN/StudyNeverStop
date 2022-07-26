#模拟手机通讯录
phone=set()
for i in range(5):
    info=input(f'请输入第{i+1}个朋友的姓名和手机号码:')
    phone.add(info)
for item in phone:
    print(item)
