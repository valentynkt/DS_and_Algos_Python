from node import DoublyNode


class DoublyLinkedList:
    """
    A doubly linked list implementation.

    Structure visualization:
        None <─ [HEAD] ⇄ [Node] ⇄ [Node] ⇄ [TAIL] ─> None

    Key invariants that MUST always be true:
        1. If A.next == B, then B.prev == A (bidirectional consistency)
        2. head.prev is always None
        3. tail.next is always None
        4. If list is empty: head == tail == None
        5. If list has one element: head == tail (same node)

    Time Complexity Summary:
        - Access by index: O(n)
        - Search: O(n)
        - Insert at head/tail: O(1)
        - Insert at index: O(n)
        - Delete head/tail: O(1)  <-- THIS is the key advantage over singly linked
        - Delete by value: O(n) search + O(1) removal
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # ==================== BASIC QUERIES ====================

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    # ==================== ITERATION ====================

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current is not None:
            yield current
            current = current.prev

    # ==================== INSERTION ====================

    def prepend(self, val):
        new_node = DoublyNode(val)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node
        self.count += 1

    def append(self, val):
        new_node = DoublyNode(val)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.count += 1

    def insert(self, index, val):
        if index < 0 or index > self.count:
            return False
        elif index == 0:
            self.prepend(val)
            return True
        elif index == self.count:
            self.append(val)
            return True

        new_node = DoublyNode(val)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next.prev = new_node
        new_node.prev = prev
        prev.next = new_node
        self.count += 1
        return True

    # ==================== ACCESS ====================
    def get(self, index):
        if index < 0 or index >= self.count:
            return None
        if index >= self.count // 2:
            current = self.tail
            for _ in range(self.count - 1 - index):
                current = current.prev
            return current
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def find(self, val):
        for i, item in enumerate(self):
            if item.val == val:
                return i
        return -1

    # ==================== DELETION ====================

    def delete(self, val):
        index = self.find(val)
        if index == -1:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            current = self.get(index)

            # prev always exists (index != 0)
            current.prev.next = current.next

            if current.next:
                current.next.prev = current.prev
            else:
                # current is tail
                self.tail = current.prev

        self.count -= 1
        return True

    def pop(self):
        item = None
        if self.size() == 0:
            return None
        elif self.size() == 1:
            item = self.head
            self.tail = None
            self.head = None
        else:
            item = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
        self.count -= 1
        return item.val

    def pop_first(self):
        item = None
        if self.size() == 0:
            return None
        elif self.size() == 1:
            item = self.head
            self.tail = None
            self.head = None
        else:
            item = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
        self.count -= 1
        return item.val
