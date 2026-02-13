# 作者: 王道 龙哥
# 2026年02月13日15时44分34秒
# xxx@qq.com

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []  # 辅助队列

    def insert_node(self, value):
        """
        插入一个新结点
        :param value:插入的值
        :return:
        """
        new_node = TreeNode(value)
        self.queue.append(new_node)  # 入队
        if self.root is None:
            self.root = new_node  # 树为空，就作为树根
        else:
            if self.queue[0].left is None:
                self.queue[0].left = new_node  # 新结点作为左孩子
            else:
                self.queue[0].right = new_node  # 新结点作为右孩子
                self.queue.pop(0)  # 出队

    def pre_order(self, current_node: TreeNode):
        """
        前序遍历，深度优先遍历
        :param current_node:
        :return:
        """
        if current_node:
            print(current_node.value, end=' ')
            self.pre_order(current_node.left)
            self.pre_order(current_node.right)

    def mid_order(self, current_node: TreeNode):
        if current_node:
            self.mid_order(current_node.left)
            print(current_node.value, end=' ')
            self.mid_order(current_node.right)

    def last_order(self, current_node: TreeNode):
        if current_node:
            self.last_order(current_node.left)
            self.last_order(current_node.right)
            print(current_node.value, end=' ')

    def level_order(self):
        queue = deque()  # 双端队列，使用双向链表来实现的
        queue.append(self.root)
        while queue:
            node:TreeNode=queue.popleft()
            print(node.value,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.insert_node(i)
    tree.pre_order(tree.root)
    print('\n-----------------------------')
    tree.mid_order(tree.root)
    print('\n-----------------------------')
    tree.last_order(tree.root)
    print('\n-----------------------------')
    tree.level_order()
