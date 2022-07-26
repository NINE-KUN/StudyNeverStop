#模拟12306火车票订票下单
dict_ticket={'G1569':['北京南-天津南','18：05','18:39','00：34'],
             'G1567':['北京南-天津南','18：15','18:49','00：34'],
             'G8917':['北京南-天津南','18：20','19:19','00：59'],
             'G203':['北京南-天津南','18：35','19:09','00：34']}
print('车次\t\t\t出发站\t\t\t\t出发时间\t\t\t到达时间\t\t\t历时时长')
for item in dict_ticket:
    print(item,end=' ')#关键字参数(键的值)
    for i in dict_ticket[item]:#根据键获取值
        print(i,end='\t\t\t')
    print()#换行
#输入要购买的车次
train_no=input('请输入要购买的车次:')
float=True
for d in dict_ticket:
    if train_no==d:
        float=True
        person=input('请输入乘车人，如果是多人请使用逗号分隔:')
        s=f'您已购买了{train_no}次列车'
        s_info=dict_ticket[train_no]#获取车次详细信息
        s+=s_info[0]+' '+s_info[1]+'\t开'#s_info[0]出发站 s_info[1]出发时间
        print(f'{s}请{person}尽快取走纸质车票')
    else:
        float=False
if not float:
    print('对不起您输入的车次有误')