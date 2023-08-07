# 有n个人(n<100)围成一圈每次从1数起数到3就把那个人提出圈子，直到剩下最后1个人
# 输入:输入人数n输出:最后留下那个人的初始位置。|
# 举例:
# 输入人数5，依次编号为 [1,2,3,4,5]第1个提出后，[1,2,4,5]第2个提出后，[2,4,5]
# 第3个提出后。[2,4]第4个提出后，[4]最后，输出结果是4。

def lastMan(n,nlist):
    while len(nlist) > 1:
        for i in range(2):
            nlist.append(nlist.pop(0))
        nlist.pop(0)
    return nlist.pop()


if __name__ == '__main__':
    print(lastMan(5,[1,2,3,4,5]))



