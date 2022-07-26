# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  1:31

# 选择结构
AgoMoney = 100000
F = '否'
T = '是'
Save = '存钱'
TakeMoney1 = int(input('请输入取款金额'))
if TakeMoney1 <= AgoMoney:
    print('请取走钞票')
    A = input('是否需要其他操作')
    if A == T:
        Operate = input("请输入需要的操作：存钱或取款")
        if Operate == Save:
            Save = int(input("请输入要存款的金额"))
            A = input('是否需要其他操作')
            if A == T:
                TakeMoney2 = int(input('请输入取款金额'))
                if TakeMoney2 <= Save+AgoMoney-TakeMoney1:
                    print('请取走钞票')
                else:
                    print('余额不足')
        else:
            TakeMoney3 = int(input('请输入取款金额'))
            if TakeMoney3 <= AgoMoney-TakeMoney1:
                print('请取走钞票')
            else:
                print('余额不足')
    else:
        print('已退卡，请取走银行卡')
else:
    print('余额不足')
    A = input('是否需要其他操作')
    if A == T:
        Operate = input("请输入需要的操作：存钱或取款")
        if Operate == Save:
            Save = int(input("请输入要存款的金额"))
        else:
            TakeMoney3 = int(input('请输入取款金额'))
            if TakeMoney3 <= AgoMoney:
                print('请取走钞票')
            else:
                print('余额不足')
    else:
        print('已退卡，请取走银行卡')

        print('----------双分支结构----------')

    cm = int(input('请输入一个整数'))
    if cm % 2 == 0:
        print('该数为偶数')
    else:
        print('该数为奇数')

        print('----------多分枝结构----------')
        """
        从键盘输入一个整数成绩
        100-90 A级
        89-80 B级
        79-70 C级
        69-60 D级
        59-0 E级
        """
        score = int(input('请输入您的成绩'))

        if score >= 90 and score <= 100 :
            print('您的成绩为A级')
        elif 80 <= score <= 89:
            print('您的成绩为B级')
        elif 70 <= score <= 79:
            print('您的成绩为C级')
        elif 60 <= score <= 69:
            print('您的成绩为D级')
        elif 0 <= score <= 59:
            print('您的成绩为E级')
        else : print('您输入的成绩不存在')






