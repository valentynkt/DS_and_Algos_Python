from itertools import count


class MinStack:
    def __init__(self) -> None:
        self.data = []
        self.count = 0

    def push(self, val: int) -> None:
        if self.count == 0 or self.data[-1][1] > val:
            self.data.append((val, val))
        else:
            self.data.append((val, self.data[-1][1]))
        self.count += 1

    def pop(self) -> None:
        if self.count != 0:
            item = self.data[-1]
            del self.data[-1]
            self.count -= 1
            return item
        return None

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
