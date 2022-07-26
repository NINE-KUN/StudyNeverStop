#格式化输出商品名称和单价
def show(lst):
    for item in lst:
        for i in item:
            print(i, end='      ')
        print()
lst=[['01','烘烤箱','美的',5000],
     ['02','洗衣机','海尔',8000],
     ['03','燃气灶','老板',7000]]
print('编号\t\t名称\t\t\t品牌\t\t单价')
show(lst)
print('-------------字符串格式化操作-------------------')
print('编号\t\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    item[0]='0000'+item[0]
    item[3]='￥{:.2f}'.format(item[3])#{:.2f}保留两位小数
show(lst)