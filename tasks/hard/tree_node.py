"""
Реализовать алгоритм двоичного дерево поиска

Бинарное дерево поиска (BST) — это дерево, в котором все узлы следуют указанным
ниже свойствам. Левое поддерево узла имеет ключ, меньший или равный ключу его
родительского узла. Правое поддерево узла имеет ключ больше, чем ключ его
родительского узла. Таким образом, BST делит все свои поддеревья на два сегмента:
левое поддерево и правое поддерево и может быть определено как -
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)


https://tproger.ru/translations/binary-search-tree-for-beginners/
"""

from typing import Optional


class TreeNode:
    value: int
    parent: Optional['TreeNode']
    left_child: Optional['TreeNode']
    right_child: Optional['TreeNode']

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

    def has_left(self):
        return self.left_child is not None

    def has_right(self):
        return self.left_child is not None

    def is_root(self):
        return self.parent is None


class Tree:
    root: Optional[TreeNode]

    def __init__(self):
        self.root = None

    def put(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._put(value, self.root)

    def _put(self, value: int, current_node: TreeNode):
        if value < current_node.value:
            if current_node.has_left():
                self._put(value, current_node.left_child)
            else:
                new_node = TreeNode(value)
                new_node.parent = current_node
                current_node.left_child = new_node
        else:
            if current_node.has_right():
                self._put(value, current_node.right_child)
            else:
                new_node = TreeNode(value)
                new_node.parent = current_node
                current_node.right_child = new_node

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value: int, current_node: TreeNode):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.has_left():
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.has_right():
            return self._search(value, current_node.right_child)
        else:
            return False


tree = Tree()
tree.put(21)
tree.put(32)
tree.put(27)
tree.put(37)
