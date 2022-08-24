# '''首先创建迷宫的数据结构'''
#
#
# class Maze:
#     '''从文件中将迷宫数据读取 保存在rowlist 然后把rowlist 保存在self.mazelist '''
#     def __init__(self, mazeFileName):
#         rowsInMaze = 0
#         columnsInMaze = 0
#         self.mazelist = []
#         mazeFile = open(mazeFileName, 'r')
#         rowsInMaze = 0
#         for line in mazeFile:
#             rowList = []
#             col = 0
#             for ch in line[:-1]:
#                 rowList.append(ch)
#                 if ch == 's':
#                     self.startRow = rowsInMaze
#                     self.startCol = col
#                 col = col + 1
#             rowsInMaze = rowsInMaze + 1
#             self.mazelist.append(rowList) #保存矩阵
#             columnsInMaze = len(rowList)

