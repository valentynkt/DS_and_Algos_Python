class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.count = 0
        self.data = [None] * capacity

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def append(self, val):
        if self.count == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.count] = val
        self.count += 1

    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        val = self.data[self.count]
        self.data[self.count] = None
        return val

    def get(self, index):
        if index < 0 or index >= self.count:
            return None
        return self.data[index]

    def set(self, index, val):
        if index < 0 or index >= self.count:
            return False
        self.data[index] = val
        return True

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.count):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
