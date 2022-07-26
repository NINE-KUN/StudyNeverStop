# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  15:54

#list3 调用calc2模块 中的add 如果不在calc2中写入if __name__=='__main__': 则calc2运算结果也会在list3运算时显示
import calc2
print(calc2.add(100,200))