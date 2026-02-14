import pytest


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i = j = write_idx = 0
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[write_idx], i = nums1_copy[i], i + 1
            else:
                nums1[write_idx], j = nums2[j], j + 1
            write_idx += 1
        nums1[write_idx:] = nums1_copy[i:m] + nums2[j:n]


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
