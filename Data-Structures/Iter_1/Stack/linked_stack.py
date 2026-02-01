from node import Node


class LinkedStack:
    def __init__(self):
        self._top = None
        self._count = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self._top
        self._top = new_node
        self._count += 1

    def pop(self):
        if self.is_empty():
            return None
        val = self._top.val
        self._top = self._top.next
        self._count -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self._top.val

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._count

    def __len__(self):
        return self.size()

    def __str__(self):
        items = []
        current = self._top
        while current:
            items.append(str(current.val))
            current = current.next
        return "top -> " + " -> ".join(items) + " -> None"
