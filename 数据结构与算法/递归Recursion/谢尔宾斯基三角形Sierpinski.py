'''分型构造，平面称谢尔宾斯基三角形，立体称谢尔宾斯基金字塔
    实际上，真正的谢尔宾斯基三角形时完全不可见的，其面积为0，
    但周长无穷，是介于一维和二维度之间的分数维(约1.585维)构造
    由于无法真正做出谢尔宾斯基三角形，只能做有限的近似图形'''

import turtle

def sierpinski(degree,points):
    colormap =['blue','red','green','white','orange','bule']
    drawTriangle(points,colormap[degree])
    if degree>0:
        sierpinski(degree - 1,
                   {'lift':})
