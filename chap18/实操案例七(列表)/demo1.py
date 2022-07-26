#根据星座测试性格特点
#创建星座列表
constellation=['射手座','天秤座','水瓶座','金牛座','天蝎座']
#创建性格列表
nature=['全是优点','一无是处','不太了解','沉稳慢热','有仇必报']
#将两个列表转成集合
a=zip(constellation,nature)
for item in a:
    print(item) #打包后为元组
d=dict(zip(constellation,nature))
for item in d:
    print(item,d[item]) #转换为字典
key=input('请输入您的星座名称:')
float=True
for item in d:
    if key==item:
        float=True
        print(key,'性格特点为：',d.get(key))
        break
    else:
        float=False
if not float:
    print('对不起您输入的星座有误')