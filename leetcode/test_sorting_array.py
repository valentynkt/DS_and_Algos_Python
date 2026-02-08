from __future__ import annotations


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def bubble_sort(self, nums: List[int]) -> List[int]:
        swapping = True
        end = len(nums)
        while swapping:
            swapping = False
            for j in range(1, end):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    swapping = True
            end -= 1
        return nums

    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        return self.merge(
            self.merge_sort(nums[:middle]), self.merge_sort(nums[middle:])
        )

    def merge(self, left: List[int], right: List[int]):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


import pytest


@pytest.fixture
def s():
    return Solution()


def test_basics(s):
    assert s.sortArray([5, 3, 8, 2, 1]) == [1, 2, 3, 5, 8]


def test_already_sorted(s):
    assert s.sortArray([1, 2, 3]) == [1, 2, 3]


def test_reverse(s):
    assert s.sortArray([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates(s):
    assert s.sortArray([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_single(s):
    assert s.sortArray([1]) == [1]


def test_empty(s):
    assert s.sortArray([]) == []


def test_negatives(s):
    assert s.sortArray([-1, 3, -5, 2]) == [-5, -1, 2, 3]
