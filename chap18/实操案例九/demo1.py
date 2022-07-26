# 统计字符串中出现指定字符的次数
def get_count(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:#忽略大小写
            count += 1
    return count
if __name__ == '__main__':
    s='hellopython,HellowJava,hElLoWC#'
    ch=input('请输入要统计的字符:')
    count=get_count(s,ch)
    print(f'{ch}在{s}中出现的次数为:{count}')

