import pytest


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        new_arr_size = len(nums) * 2
        result = [0] * new_arr_size
        j = new_arr_size - 1
        for i, num in enumerate(nums):
            result[i] = result[i + len(nums)] = num

        return result


@pytest.fixture
def s():
    return Solution()


def test_basics(s):
    assert s.getConcatenation([1, 4, 1, 2]) == [2, 10, 20, 20, 40]


def test_basics2(s):
    assert s.getConcatenation([22, 21, 20, 1]) == [22, 21, 20, 1, 22, 20, 1]
