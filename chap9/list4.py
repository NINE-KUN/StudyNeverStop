# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:43

# 函数的参数定义
'''函数定义默认值参数
   函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
'''
def ref(a,b=10):  #b称为默认值参数
    print(a,b)
ref(100) #只传递1个参数 b采用默认值10
ref(20,30) #两个实参与形参不同 按位置传参

