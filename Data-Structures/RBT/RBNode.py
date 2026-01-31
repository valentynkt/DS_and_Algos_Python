from hmac import new


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left: RBNode | None = None
        self.right: RBNode | None = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.left = pivot.left
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def insert(self, val):
        new_node = RBNode(val)
        new_node.red = True
        new_node.left = self.nil
        new_node.right = self.nil
        current = self.root
        parent = None
        while current != self.nil:
            parent = current
            if new_node.val == current.val:
                return
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
            return
        if new_node.val < parent.val:
            parent.left = new_node
            return
        elif new_node.val > parent.val:
            parent.right = new_node
