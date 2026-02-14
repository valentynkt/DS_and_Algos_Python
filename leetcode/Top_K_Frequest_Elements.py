from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        occurance = defaultdict(int)

        for i in nums:
            occurance[i] += 1

        buckets = [[] for _ in range(len_nums + 1)]
        for item, frequence in occurance.items():
            buckets[frequence].append(item)

        result = []
        for freq in range(len_nums, 0, -1):
            for num in buckets[freq]:
                result.append(nums)
                if len(result) == k:
                    return result
        return None
