from typing import Any

from node import Node


class LLQueue:
    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def __bool__(self) -> bool:
        return self._head is not None

    def is_empty(self) -> bool:
        return self._head is None

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.val
            node = node.next

    def __repr__(self) -> str:
        values = [str(val) for val in self]
        return " <- ".join(values)

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._head.val

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)
        self._add_to_tail(new_node)

    def dequeue(self) -> Any:
        return self._remove_from_head()

    def _add_to_tail(self, node: Node) -> None:
        self._length += 1
        if self._head is None:
            self._head = node
            self._tail = node
            return
        self._tail.set_next(node)
        self._tail = node

    def _remove_from_head(self) -> Any:
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        value = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._length -= 1
        return value
