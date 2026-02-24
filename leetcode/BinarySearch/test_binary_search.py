import pytest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def _search(left: int, right: int):
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if right - left <= 1:
                return -1
            if target > nums[middle]:
                result = _search(middle, right)
            else:
                result = _search(left, middle)
            return result

        result = _search(0, len(nums))

        return result


@pytest.fixture
def s():
    return Solution()


def test_basic2(s):
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
