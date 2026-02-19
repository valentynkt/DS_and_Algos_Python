# Difficulty: Medium
# Self-solved: ~60-65% — REVISIT
# Pattern: Set + sequence start detection + count forward
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        max_so_far = 1
        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                while num + length in set_nums:
                    length += 1
                max_so_far = max(max_so_far, length)

        return max_so_far
