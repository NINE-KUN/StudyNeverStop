'''通过递归作图来展现递归调用的视觉影响'''

''' python的海归作图系统turtle module
    python内置，随时可用，以LOGO语言的创意为基础
    其意象为模拟海归在沙滩上爬行而留下的足迹
    爬行：forward(n);backward(n)
    转向:left(a);right(a)
    抬笔放笔：penup();pendown()
    笔属性：pensize(s);pencolor(c)'''

import turtle

t = turtle.Turtle()
# def drawSpiral(t,lineLen):
#     if lineLen > 0:
#         t.forward(lineLen)
#         t.right(90)
#         drawSpiral(t,lineLen-5)
# drawSpiral(t,100)
# turtle.done()
'''分形Fractal 
    一个粗糙或者零碎的几何形状，可以分成数个部分，且每一部分都(至少近似地)是整体缩小后的形状，即具有自相似的性质'''


def tree(branch_len):
    if branch_len > 5:  # 树干低于5停止 递归结束条件
        t.forward(branch_len)  # 画树干
        t.right(20)  # 右倾斜20度
        tree(branch_len - 15)  # 递归调用 画右边的树枝 树枝长度=树干-15
        t.left(40)  # 向左倾斜40度
        tree(branch_len - 15)  # 递归调用 画左边的树枝 树枝长度-树干长度-15
        t.right(20)  # 向右回20度
        t.backward(branch_len)  # 海归退回原位置


t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('black')
t.pensize(2)
tree(75)  # 画树干长度75的二叉树
t.hideturtle()
turtle.done()
