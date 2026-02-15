from collections import defaultdict

import pytest


# This is a brute force solution with O n^2 we could improve the solution.
# We could use hash function, to store key-the number, value it index.
# Than we could have just one for loop. And using formula : needed_num = target - current_num. check if we have this needed_num in hash.
class Solution:
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        nums_dict = defaultdict(int)
        for i in range(0, len(nums)):
            needed_num = target - nums[i]
            if needed_num in nums_dict:
                return [nums_dict[needed_num], i]
            nums_dict[nums[i]] = i
        return []

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


@pytest.fixture
def s():
    return Solution()


def test_basics2(s):
    assert s.twoSum2([3, 4, 5, 6], 7) == [0, 1]
    assert s.twoSum2([4, 5, 6], 10) == [0, 2]
    assert s.twoSum2([5, 5], 10) == [0, 1]
