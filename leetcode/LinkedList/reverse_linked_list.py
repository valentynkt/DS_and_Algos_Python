from getopt import gnu_getopt


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recurseReverseList(head)

    def recurseReverseList(self, node: ListNode) -> ListNode:
        if node is None or node.next is None:
            return node
        new_head = self.recurseReverseList(node.next)
        node.next.next = node
        node.next = None
        return new_head
