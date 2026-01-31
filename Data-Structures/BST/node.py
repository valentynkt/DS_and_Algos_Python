from concurrent.interpreters import get_main


class BSTNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

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

        if self.left is not None and self.right is not None:
            right_min = self.right.get_min()
            self.val = right_min
            self.right = self.right.delete(right_min)
            return self

        # One Child case (Right)
        if self.left is None:
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
