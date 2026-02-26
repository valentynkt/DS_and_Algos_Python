from collections import Counter, defaultdict


class Solution:
    # Boyer-Moore
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
