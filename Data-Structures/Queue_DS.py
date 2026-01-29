class Queue:
    def __init__(self) -> None:
        self.items: list = []

    def __repr__(self) -> str:
        return f"Stack({self.items})"

    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return len(self.items) > 0

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.insert(0, item)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
