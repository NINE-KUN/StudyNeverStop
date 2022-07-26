#京东购物流程
print('------------------------商品入库-------------------------------')
lst=[]
for i in range(0,5):
    goods=input('请输入商品编号和商品名称进行入库操作，每次只可以输入一件商品：\n')
    lst.append(goods)
for item in lst:
    print(item)

print('--------------------添加到购物车------------------------')
cart=[]
while True:
    num=input('请输入要购买的商品编号')
    for item in lst:
        if item.find(num)!=-1:
            cart.append(item)
            break#退出for循环
    if num=='q':
        break#退出while True循环
print('您的购物车已经选好商品为：')
for m in cart:
    print(m)
print('---------------逆序输出-------------')
for i in  range(len(cart)-1,-1,-1):
    print(cart[i])