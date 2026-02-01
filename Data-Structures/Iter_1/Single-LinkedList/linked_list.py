from node import Node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
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
        if self.head is None:
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.count += 1

    def get(self, index):
        if index < 0 or index >= self.count:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def insert(self, index, val):
        if index < 0 or index > self.count:
            return False
        if index == 0:
            self.prepend(val)
            return True
        if index == self.count:
            self.append(val)
            return True

        new_node = Node(val)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.count += 1
        return True

    def delete(self, val):
        index = self.find(val)
        if index == -1:
            return False
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            prev = self.get(index - 1)
            prev.next = prev.next.next
            if not prev.next:
                self.tail = prev
        self.count -= 1
        return True

    def find(self, val):
        for i, item in enumerate(self):
            if item.val == val:
                return i
        return -1
