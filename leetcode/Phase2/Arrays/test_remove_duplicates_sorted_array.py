import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow += 1 return slow + 1


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.removeDuplicates([0, 0, 1, 1, 1, 2, 3, 3, 4]) == 5
