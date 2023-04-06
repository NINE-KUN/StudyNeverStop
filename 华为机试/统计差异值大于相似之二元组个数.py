'''题目描述
题目描述: 对于任意两个正整数 A 和 B，定义它们之间的差异值和相似值:
差异值: A、B 转换成二进制后，对于二进制的每一位，对应位置的 bit 值不相同则为 1，否则为0;
相似值: A、B 转换成二进制后，对于二进制的每一位，对应位置的 bit 值都为 1则为 1，否则为0;
现在有 n 个正整数 A 到 A(n-1)，问有多少对(i,j)(0 <= i < j < n)，Ai和 Aj 的差异值大于相似值。
假设 4=5，B=3；
则 A 的二进制表示 101；
则 B 的二进制表示 011；
则 A 与 B 的差异值二进制为 110，十进制等于 6；
则 A 与 B 的相似值二进制为 001，十进制等于 1；
有 A 与 B 的差异值大于相似值，满足条件

输入描述
输入:一个n 接下来n个正整数
数据范围: 1 <= n <= 10^5，1 <= A[i] < 2^30
输出描述
输出: 满足差异值大于相似值的对数

示例一
输入：
4
4 3 5 2
输出：
4'''

while 1:
    try:
        n = int(input())
        numList = list(map(int, input().split()))

        count = 0
        for i in range(n):
            # 0 <= i < j < n
            for j in range(i+1, n, 1):
                if numList[i] ^ numList[j] > numList[i] & numList[j]:
                    count += 1
                    # print((i, j))
        print(count)
    except Exception as e:
        break

