class ArrayStack:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        return not self._data

    def size(self):
        return len(self._data)

    def __len__(self):
        return self.size()

    def __str__(self):
        return f"Stack: {self._data} <- top"
