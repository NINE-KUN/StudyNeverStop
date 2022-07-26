#将指定的十进制数转化为二进制、八进制、十六进制
def fun():
    num=int(input('请输入一个十进制的整数'))#将str类型转换为int类型
    print(num,'的二进制数位:',bin(num))#第一种写法 使用了位置可变的位置参数
    print(str(num)+'的二进制数为:'+bin(num))#第二种写法 使用了“+”作为连接符 注意：+左右均为str类型
    print('%s的二进制数为：%s' % (num,bin(num)))#第三种写法 格式化字符串
    print('{0}的二进制数为:{1}'.format(num,bin(num)))#第三种写法 格式化字符串
    print(f'{num}的二进制数为:{bin(num)}')#第三种 格式化字符串
    print('--------------------------------------------------------------')
    print(f'{num}的八进制数位:{oct(num)}')
    print(f'{num}的十六进制数位:{hex(num)}')

if __name__ == '__main__':
    while True:
        try:
          fun()
          break
        except:
            print('只能输入整数，请重新输入')
    try:
        fun()

    except:
        print('程序出错，请重新输入')
        fun()