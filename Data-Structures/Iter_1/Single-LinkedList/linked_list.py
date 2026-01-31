from node import Node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def size(self):
        return self.count

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def append(self, val):
        if self.head is None:
            self.head = Node(val)

        self.count += 1

    def get(self, index):
        pass

    def insert(self, index, val):
        pass

    def delete(self, val):
        pass

    def find(self, val):
        pass
