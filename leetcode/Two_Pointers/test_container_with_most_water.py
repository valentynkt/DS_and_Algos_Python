import pytest


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            cur_area = min(heights[i], heights[j]) * (j - i)
            if max_area < cur_area:
                max_area = cur_area
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
        return max_area


@pytest.fixture
def s():
    return Solution()


# --- Basic examples from problem ---
def test_example1(s):
    assert s.maxArea([1, 7, 2, 5, 4, 7, 3, 6]) == 36


def test_example2(s):
    assert s.maxArea([2, 2, 2]) == 4


# --- Edge cases ---
def test_two_elements(s):
    assert s.maxArea([1, 1]) == 1


def test_tall_ends(s):
    # Walls at edges: min(5,5) * 4 = 20
    assert s.maxArea([5, 1, 1, 1, 5]) == 20


def test_one_tall_one_short(s):
    # min(1, 1000) * 1 = 1
    assert s.maxArea([1, 1000]) == 1


def test_ascending(s):
    # [1,2,3,4,5] best is min(2,5)*3=6 or min(1,5)*4=4... min(3,5)*2=6, min(4,5)*1=4
    # Actually: i=1,j=4 -> min(2,5)*3=6; i=0,j=4 -> min(1,5)*4=4; i=2,j=4 -> min(3,5)*2=6
    assert s.maxArea([1, 2, 3, 4, 5]) == 6


def test_descending(s):
    assert s.maxArea([5, 4, 3, 2, 1]) == 6
