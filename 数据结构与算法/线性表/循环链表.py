class ListNode():
    def __init__(self,data):
        self.head = data
        self.next = None
#判断列表是否为空
def isempty(self):
    return self.head == None
#在头部添加元素
def nodes_head(self,data):
    if isempty(self):
        self.head = data
        self.next = self
        return self
    else:
        newnode = ListNode(None)
        newnode.head = data
        newnode.next = self
        p = self
        while p.next != self:
            p = p.next
        p.next = newnode
        #返回头部节点
        return newnode
#尾部添加元素
def nodes_tail(self,data):
    if isempty(self):
        self.read = data
        self.next = self
    else:
        p = self
        node = ListNode(None)
        node.head = data
        while p.next != self:
            p = p.next
        p.next = node
        node.next = self
#在指定位置插入元素
def nodes_insert(self,data,num):
    if num < 1:
        return False
    elif num == 1:
        nodes_head(self, data)
        return True
    else:
        p = self
        while num-2:
            num = num -1
            p = p.next
        node  = ListNode(None)
        node.head = data
        q = p.next
        p.next = node
        node.next = q
#删除指定元素
def nodes_remove(self,data):
    if isempty(self):
        return False
    else:
        p = self
        if p.head == data:
            while p.next != self:
                p = p.next
            p.next = self.next
            return  True
        else:
            p = self
            while p.next != self:
                if p.next.head == data:
                    q = p.next
                    p.next = q.next
                    return True
                p = p.next

if __name__=='__main__':
    #初始化循环链表
    listnode = ListNode(None)
    for i in range(5):
        listnode = nodes_head(listnode,i)
    nodes_tail(listnode,8)
    p = listnode
    nodes_insert(listnode,9,3)
    nodes_remove(listnode,2)
    while p.next != listnode:
        print(p.head)
        p = p.next
    print(p.head)
