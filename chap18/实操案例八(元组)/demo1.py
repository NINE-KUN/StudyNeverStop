#我的咖啡馆你来做主（使用元组实现）
coffee_name=('日晒埃塞','水洗埃塞','肯尼亚','云南','红标瑰夏')
print('欢迎光临WULI COFFEE')
print('本店经营咖啡有:')
for index,item in enumerate(coffee_name):#获取index元组索引 获取item元组内容
    print(index+1,'.',item,end='     ')
index=int(input('\n请输入您喜欢的咖啡编号:'))
if 0<=index<=len(coffee_name):
    print(f'您的咖啡[{coffee_name[index-1]}]好了，请您慢用')
else:
    print('您输入的编号不存在')
