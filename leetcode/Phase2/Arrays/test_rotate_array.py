from collections import defaultdict

import pytest


class Solution:
    # we may use dict, firstly go through each element, for key we will have targeted index (current index + k) and for value we will have number,
    # Than in antorhe array we will go through the dict to rebuild the array. it will not be O 1 space, but still good O speed.
    # the solution 1, is ready with description above. now trying to reach O 1 space
    # we could determine
    def rotate(self, nums: list[int], k: int) -> None:
        arr_dict = defaultdict(int)
        for i in range(0, len(nums)):
            new_pos = (i + k) % (len(nums))
            arr_dict[new_pos] = nums[i]
        for key, value in arr_dict.items():
            nums[key] = value


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
