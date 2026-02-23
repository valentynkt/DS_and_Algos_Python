import pytest


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


@pytest.fixture
def s():
    return Solution()


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_basic(s):
    list1 = build([1, 2, 4])
    list2 = build([1, 3, 5])
    assert to_list(s.mergeTwoLists(list1, list2)) == [1, 1, 2, 3, 4, 5]


def test_empty(s):
    list1 = build([])
    list2 = build([1, 2])
    assert to_list(s.mergeTwoLists(list1, list2)) == [1, 2]
