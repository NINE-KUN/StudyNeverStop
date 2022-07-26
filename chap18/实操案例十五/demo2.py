#模拟淘宝客服
def find_answer(question):
    with open('replay.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline()
            if not line:#或者用if line==''到文件末尾
                break
            #字符串分割
            keyword=line.split('|')[0]#分割后问题
            reply=line.split('|')[1]#分割后的答案
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question=input('Hi,您好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧')
    while True:
        if question=='bye':
            break
        #开始在文件中查找
        replay=find_answer(question)
        if not replay:#如果回复的是False， not False-->True
            question=input('小蜜不知道您在说什么，您可以问一些关于订单，物流，账户，支付等问题(退出请输入bye)')
        else:
            print(replay)
            question=input('小主您可以继续问一些关于订单，物流，账户，支付等问题(退出请输入bye)')
    print('小主再见')
