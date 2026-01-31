class BSTNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

    def exists(self, val):
        if self.val is None:
            return False
        if self.val == val:
            return True
        child = self.left if val < self.val else self.right
        return child is not None and child.exists(val)

    def inorder(self, visited):
        if self.left is not None:
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited

    def postorder(self, visited):
        if self.left is not None:
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        if self.val is not None:
            visited.append(self.val)
        return visited

    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited

    @classmethod
    def from_preorder(cls, values):
        if not values:
            return None
        root = cls(values[0])
        for val in values[1:]:
            root.insert(val)
        return root

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
            return self
        elif val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self

        elif self.left is not None and self.right is not None:
            right_min = self.right.get_min()
            self.val = right_min
            self.right = self.right.delete(right_min)
            return self

        # One Child case (Right)
        elif self.left is None:
            # Right is None here
            return self.right
        elif self.right is None:
            return self.left

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def insert(self, val):
        if self.val == val or self.val is None:
            self.val = val
            return
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
