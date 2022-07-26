"""
功能∶实现单链表的构建和功能操作重点代码
"""


# 创建节点类
class Node:
    """
    思路∶将自定义的类视为节点的生成类,实例对象中
    包含数据部分和指向下一个节点的n e x t
    """

    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系


class LinkListManager:
    def __init__(self):
        """
        初始化链表﹐标记一个链表的开端(即头结点)﹐以便于获取后续的节点
        """
        self.head =Node(None)

    def init_list(self, list_):
        pointer = self.head  # 相当于指针，初始指向头部
        for item in list_:
            pointer.next = Node(item)  # 将头部的next指向node
            pointer = pointer.next  # 指针移动到下一个值

    def show_list(self):
        """
        遍历链表
        :return:
        """
        pointer_value = self.head.next  # 将指针从头部移动到第一个值
        while pointer_value is not None:
            print(pointer_value.val)
            pointer_value = pointer_value.next  # 将指针向下移动

    def is_empty(self):
        """
        判断链表是否为空
        :return: bool
        """
        if self.head.next is None:
            return True
        return False

    def clear(self):
        """
        清空链表
        :return:
        """
        self.head.next = None

    def append_end_value(self, value):
        """
        尾部插入(尾插法)
        :return:
        """
        pointer = self.head
        while pointer.next is not None:  # 将指针移动到最后的节点上
            pointer = pointer.next
        pointer.next = Node(value)  # 在最后的节点上插值

    def append_start_value(self, value):
        """
        头部插入(头插法)
        :return:
        """
        node = Node(value)  # 定义一个节点
        node.next = self.head.next  # 将新节点next链接到第一个节点（不算头部）
        self.head.next = node  # 将头部节点的next的链接到node

    def count_index(self):
        """
        查看节点数
        :return: 节点数
        """
        count = 0
        pointer = self.head
        while pointer.next is not None:
            count += 1
            pointer = pointer.next
        return count

    def insert_value(self, index, value):
        """
        某个位置插入(按照索引规则从0开始)
        :return:
        """
        if self.count_index() < index:
            self.append_end_value(value)
        elif index < 0:
            self.append_start_value(value)
        else:
            pointer = self.head
            for i in range(index):
                pointer = pointer.next  # 将指针移动到index的前一个节点
            node = Node(value)  # 定义一个节点
            node.next = pointer.next  #将插入位前结点的后继结点改为插入节点的后继结点
            pointer.next = node  #将插入节点改为插入位前结点的后继结点

    def remove_value(self, value):
        """
        按照值删除节点
        :param value:
        :return:
        """
        pointer = self.head
        while pointer.next and pointer.next.val != value:  # 将指针移动到value的前一个节点，若到末尾则停止
            pointer = pointer.next

        if pointer.next is None:  # 若到链表末尾，则value不在表中
            raise ValueError("value  not in linklist ")
        else:
            pointer.next = pointer.next.next#将删除位前结点的后继结点改为后继结点的后继结点

    def get_index(self, index):
        """
        根据索引获取值
        :param index: 索引
        :return: 索引对应值
        """
        return self.__get_element(index).val

    def __get_element(self, index):
        """
        根据索引获取对应的节点
        :param index: 索引
        :return: 该节点
        """
        pointer = self.head.next
        if index < 0:
            raise ValueError("index out of range")
        for i in range(index):
            if pointer.next is None:
                raise ValueError("index out of range")
            pointer = pointer.next
        return pointer

    def update(self, index, new_value):
        """
        根据索引修改值
        :param index: 索引
        :param new_value:新值
        :return:
        """
        self.__get_element(index).val = new_value


if __name__ == '__main__':  # 测试代码
    manager = LinkListManager()
    manager.init_list([1, 2, 3, 4, 5])
    manager.append_end_value(6)
    manager.append_start_value(0)
    print(manager.count_index())
    manager.insert_value(5, 88)
    manager.remove_value(88)
    print(manager.get_index(4))
    manager.update(4, 8)
    manager.show_list()
