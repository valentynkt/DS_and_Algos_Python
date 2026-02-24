import pytest


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        end = len(nums) - 1
        while i <= end:
            if nums[i] == val:
                if nums[end] == val:
                    end -= 1
                    continue
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1

        return i


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.removeElement([3, 2, 2, 3], 3) == 2
