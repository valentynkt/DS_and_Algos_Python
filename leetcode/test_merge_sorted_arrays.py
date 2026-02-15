import pytest


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = n + m - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1


@pytest.fixture
def s():
    return Solution()


def test_basics(s):
    nums1 = [10, 20, 20, 40, 0, 0]
    s.merge(nums1, 4, [1, 2], 2)
    assert nums1 == [1, 2, 10, 20, 20, 40]


def test_already_sorted(s):
    nums1 = [1, 2, 3, 0, 0, 0]
    s.merge(nums1, 3, [4, 5, 6], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]
