class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self) -> str:
        return self.val
