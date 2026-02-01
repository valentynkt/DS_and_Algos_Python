class DoublyNode:
    """
    A node in a doubly linked list.

    Unlike a singly linked node, this node maintains TWO references:
    - next: points to the node AFTER this one
    - prev: points to the node BEFORE this one

    This bidirectional linking is what enables O(1) operations
    when you already have a reference to a node.

    Attributes:
        val: The data stored in this node (can be any type)
        next: Reference to the next DoublyNode, or None if this is the tail
        prev: Reference to the previous DoublyNode, or None if this is the head
    """

    def __init__(self, val):
        # TODO: Initialize val, next, and prev
        self.val = val
        self.next: DoublyNode | None = None
        self.prev: DoublyNode | None = None
