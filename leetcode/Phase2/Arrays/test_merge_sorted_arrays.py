import pytest


class Solution:
    # while i < m and j < n ..... while i < m , while j < n...
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.merge([0], 0, [1], 1) == [1]
