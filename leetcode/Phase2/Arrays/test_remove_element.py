import pytest


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.removeElement([3, 2, 2, 3], 3) == 2
