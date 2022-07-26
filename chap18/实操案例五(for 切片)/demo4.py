#计算100-999之间的水仙花数(个位十位百位分别三次方和这个数相等)
import math
for i in range(100,1000):
    if math.pow((i%10),3)+math.pow((i//10%10),3)+math.pow(i//100,3)==i:
        print(i)