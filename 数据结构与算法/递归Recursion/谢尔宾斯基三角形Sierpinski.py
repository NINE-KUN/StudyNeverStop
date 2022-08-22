'''分型构造，平面称谢尔宾斯基三角形，立体称谢尔宾斯基金字塔
    实际上，真正的谢尔宾斯基三角形时完全不可见的，其面积为0，
    但周长无穷，是介于一维和二维度之间的分数维(约1.585维)构造
    由于无法真正做出谢尔宾斯基三角形，只能做有限的近似图形'''

import turtle


def sierpinski(degree, points):
    '''
    :param degree: 画多少阶的三角形
    :param points: 点的字典 描绘了三角形的轮廓
    :return:
    '''
    colormap = ['grey', 'red', 'black', 'white', 'yellow', 'orange']
    drawTriangle(points, colormap[degree])#画等边三角形轮廓
    if degree > 0:#最小规模,0直接退出
        '''减小规模:getMid边长减半
            调用自身，左上右次序'''
        sierpinski(degree - 1,
                   {'left': points['left'], #左顶点还是大三角形左顶点
                    'top': getMid(points['left'],points['top']),#上顶点是大三角形左顶点和上顶点连城边的一般
                    'right': getMid(points['left'], points['right'])})#右顶点是大三角形做顶点和右顶点连成线的一半
        sierpinski(degree - 1,
                   {'left': getMid(points['left'], points['top']),
                    'top': points['top'],
                    'right': getMid(points['top'], points['right'])})
        sierpinski(degree - 1,
                   {'left': getMid(points['left'], points['right']),
                    'top': getMid(points['top'], points['right']),
                    'right': points['right']})


t = turtle.Turtle()

'''绘制等边三角形'''
def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

'''取两个点的中间点 x坐标加起来除以2 y坐标加起来除以2'''
def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

'''外轮廓三个顶点 确定三个顶点的x，y坐标'''
points={'left':(-200,-100),
        'top':(0,200),
        'right':(200,-100)}
'''画defgree=5的三角形'''
sierpinski(5,points)
turtle.done()