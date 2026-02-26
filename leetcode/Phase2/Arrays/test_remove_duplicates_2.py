import pytest


class Solution:
    # slow/fast slow will be index of where to place, and fast will go through ellements
    # We need some additional state (variable) where we will save health = 1 in case of first occurence of duplicates
    # we will decrease the health by one. if health == 0,
    # than it is duplicates that should be replaced and where our slow should point to
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 1
        if len(nums) <= 2:
            return len(nums)
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow + 1] = nums[fast]
                slow += 1

        return slow + 1


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
