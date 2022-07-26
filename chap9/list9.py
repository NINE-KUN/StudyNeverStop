# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  13:11

def fac(n):
    if n==1:
        return 1
    else:
        res=n*fac(n-1) # 先调用fac(n-1)当n=1时 才调用n*fac(n-1)
        return res
print(fac(6))


