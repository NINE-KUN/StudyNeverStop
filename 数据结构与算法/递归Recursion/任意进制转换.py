'''通过递归的方式 实现整数转换任意进制'''
def toStr(n,base):
    convertString='0123456789ABCDEF'
    if n<base:
        return convertString[n] #最小规模
    else:
        '''除以进制基base(//base) 对进制基求余数(%base  )'''
        return toStr(n//base,base)+convertString[n%base] #减小规模调用自身
print(toStr(1453,16))