class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        suffix = [1] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(1)
                continue
            prefix.append(prefix[i - 1] * nums[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result
