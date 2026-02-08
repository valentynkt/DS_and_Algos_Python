from collections import deque

from node import Node


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def insert(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.root = new_node
            return

        self._insert_helper(self.root, val)

    def _insert_helper(self, current_node, val):
        if current_node is None:
            return Node(val)
        if val < current_node.val:
            current_node.left = self._insert_helper(current_node.left, val)
        elif val > current_node.val:
            current_node.right = self._insert_helper(current_node.right, val)
        return current_node

    def search(self, val):
        node = self.root
        while node is not None:
            if val == node.val:
                return node
            node = node.left if val < node.val else node.right
        return None

    def contains(self, val):
        return self.search(val) is not None

    def find_min(self):
        return self._find_min_node(self.root)

    def _find_min_node(self, node):
        while node is not None and node.left is not None:
            node = node.left
        return node

    def find_max(self):
        return self._find_max_node(self.root)

    def _find_max_node(self, node):
        while node is not None and node.right is not None:
            node = node.right
        return node

    def delete(self, val):
        self.root = self._delete_helper(self.root, val)

    def _delete_helper(self, node, val):
        if node is None:
            return None

        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is not None and node.right is not None:
                right_min = self._find_min_node(node.right)
                node.val = right_min.val
                node.right = self._delete_helper(node.right, right_min.val)
                return node

            return node.left if node.left else node.right
        return node

    def preorder(self):
        visited = []
        self._preorder_helper(self.root, visited)
        return visited

    def _preorder_helper(self, node, visited):
        if node is None:
            return
        visited.append(node.val)
        self._preorder_helper(node.left, visited)
        self._preorder_helper(node.right, visited)

    def inorder(self):
        visited = []
        self._inorder_helper(self.root, visited)
        return visited

    def _inorder_helper(self, node, visited):
        if node is None:
            return
        self._inorder_helper(node.left, visited)
        visited.append(node.val)
        self._inorder_helper(node.right, visited)

    def postorder(self):
        visited = []
        self._postorder_helper(self.root, visited)
        return visited

    def _postorder_helper(self, node, visited):
        if node is None:
            return
        self._postorder_helper(node.left, visited)
        self._postorder_helper(node.right, visited)
        visited.append(node.val)

    def levelorder(self):
        node = self.root
        visited = []
        if not self.root:
            return []
        q = deque([node])
        while q:
            item = q.popleft()
            visited.append(item.val)
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        return visited

    def height(self):
        root = self.root
        return self._height_helper(root)

    def _height_helper(self, node):
        if not node:
            return -1
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))

    def count_nodes(self):
        return self._count_helper(self.root)

    def _count_helper(self, node):
        if not node:
            return 0
        return 1 + self._count_helper(node.left) + self._count_helper(node.right)
