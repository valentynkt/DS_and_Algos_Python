class MaxHeap:
    def __init__(self):
        """Initialize empty heap."""
        self._data = []
        self._len = 0

    def __len__(self):
        return self._len

    def peek(self):
        """Return max element without removing. Raise IndexError if empty."""
        return self._data[0] if self._len > 0 else None

    def push(self, value):
        """Add value to heap, maintaining heap property."""
        # Step 1: append to end
        # Step 2: bubble up
        self._len += 1
        self._data.append(value)
        self._bubble_up(self._len - 1)

    def pop(self):
        """Remove and return max element. Raise IndexError if empty."""
        # Step 1: save max (root)
        # Step 2: move last element to root
        # Step 3: bubble down
        if self._len > 0:
            max_root = self._data[0]
            self._data[0] = self._data[-1]
            del self._data[-1]
            self._len -= 1
            self._bubble_down(0)
            return max_root
        return None

    # --- Index helpers ---

    def _parent(self, i):
        """Return parent index of node at index i."""
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    # --- Core helpers ---

    def _bubble_up(self, i):
        """Move node at index i up until heap property is restored."""
        while i > 0:
            parent = self._parent(i)
            if self._data[parent] < self._data[i]:
                self._data[parent], self._data[i] = self._data[i], self._data[parent]
                i = parent
            else:
                break

    def _bubble_down(self, i):
        """Move node at index i down until heap property is restored."""
        while True:
            largest = i
            left = self._left(i)
            right = self._right(i)

            if left < self._len and self._data[left] > self._data[largest]:
                largest = left
            if right < self._len and self._data[right] > self._data[largest]:
                largest = right

            if largest == i:
                break

            self._data[i], self._data[largest] = self._data[largest], self._data[i]
            i = largest
