# Difficulty: Medium
# Self-solved: ~30% — MUST REVISIT
# Pattern: Sort + fix one element + two pointers (extends Two Sum II)
# Key insight: sorting makes deduplication trivial (skip adjacent duplicates)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, r = i + 1, len(nums) - 1
            while left < r:
                total = nums[i] + nums[left] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[left], nums[r]])
                    while left < r and nums[left] == nums[left + 1]:
                        left += 1
                    while left < r and nums[r] == nums[r - 1]:
                        r -= 1
                    left += 1
                    r -= 1
                elif total < 0:
                    left += 1
                else:
                    r -= 1
        return result
