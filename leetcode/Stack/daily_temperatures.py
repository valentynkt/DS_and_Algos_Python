class Solution:
    # We could consider using dictionary, where the key will be the inder, and the value will be tuple (biggest_so_far, count)
    # arr = [30, 38, 30, 36, 35, 40, 28]
    # we should initialize first element befor loop, and start at index 1
    # for i in range(0, len(arr)):
    # step 1: dict = {0: (30, 0)}
    # step 2: if arr[i] > dict[i-1][0]
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            if len(stack) == 0:
                stack.append((i, temperatures[i]))
                continue
            while len(stack) >= 1 and temperatures[i] > stack[-1][1]:
                cur_item = stack.pop()
                result[cur_item[0]] = i - cur_item[0]
            stack.append((i, temperatures[i]))
        return result
