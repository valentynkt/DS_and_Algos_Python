class MyHashMap:
    def __init__(self):
        self.count = 0
        self.capacity_exp = 3  # p = 3, so size = 2^3 = 8
        self.size = 1 << self.capacity_exp  # 8
        self.load_factor = 0.7
        self.data = [None] * self.size

    def put(self, key: int, value: int) -> None:
        if self.count / self.size > self.load_factor:
            self._resize()
        hash = self._map_key_to_hash(key)
        if self.data[hash] is not None and self.data[hash][0] == key:
            self.data[hash] = (key, value)
            return
        self.data[hash] = (key, value)
        self.count += 1
        return

    def get(self, key: int) -> int:
        hash = self._map_key_to_hash(key)
        if self.data[hash] is not None and self.data[hash][0] == key:
            return self.data[hash][1]
        return -1

    def _resize(self):
        self.capacity_exp += 1
        self.size = 1 << self.capacity_exp

        temp = [None] * self.size
        for item in self.data:
            if item is not None:
                new_hash = self._map_key_to_hash(item[0])
                temp[new_hash] = (item[0], item[1])
        self.data = temp
        return

    def _map_key_to_hash(self, key):
        return ((key * 2654435769) & 0xFFFFFFFF) >> (32 - self.capacity_exp)

    def remove(self, key: int) -> None:
        hash = self._map_key_to_hash(key)
        if self.data[hash] is not None and self.data[hash][0] == key:
            self.data[hash] = None
            self.count -= 1
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key
