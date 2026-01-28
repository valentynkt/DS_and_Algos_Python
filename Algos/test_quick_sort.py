from quick_sort import partition, quick_sort


class TestPartition:
    """Test cases for the partition helper function."""

    def test_partition_two_elements_sorted(self):
        arr = [1, 2]
        pivot_idx = partition(arr, 0, 1)
        assert arr[pivot_idx] == 2
        assert all(arr[i] <= arr[pivot_idx] for i in range(pivot_idx))

    def test_partition_two_elements_unsorted(self):
        arr = [2, 1]
        pivot_idx = partition(arr, 0, 1)
        assert arr[pivot_idx] == 1
        assert all(arr[i] <= arr[pivot_idx] for i in range(pivot_idx))

    def test_partition_three_elements(self):
        arr = [3, 1, 2]
        pivot_idx = partition(arr, 0, 2)
        pivot = arr[pivot_idx]
        assert all(arr[i] <= pivot for i in range(pivot_idx))
        assert all(arr[i] >= pivot for i in range(pivot_idx + 1, len(arr)))

    def test_partition_pivot_is_largest(self):
        arr = [1, 2, 3]
        pivot_idx = partition(arr, 0, 2)
        assert arr[pivot_idx] == 3
        assert all(arr[i] <= 3 for i in range(pivot_idx))

    def test_partition_pivot_is_smallest(self):
        arr = [2, 3, 1]
        pivot_idx = partition(arr, 0, 2)
        assert arr[pivot_idx] == 1
        assert all(arr[i] >= 1 for i in range(pivot_idx + 1, len(arr)))

    def test_partition_with_duplicates(self):
        arr = [3, 1, 2, 3, 1]
        pivot_idx = partition(arr, 0, 4)
        pivot = arr[pivot_idx]
        assert all(arr[i] <= pivot for i in range(pivot_idx))
        assert all(arr[i] >= pivot for i in range(pivot_idx + 1, len(arr)))

    def test_partition_subrange(self):
        """Partition should only affect elements between low and high."""
        arr = [9, 5, 3, 1, 8]
        partition(arr, 1, 3)
        assert arr[0] == 9  # Untouched
        assert arr[4] == 8  # Untouched

    def test_partition_single_element(self):
        arr = [42]
        pivot_idx = partition(arr, 0, 0)
        assert pivot_idx == 0
        assert arr == [42]


class TestQuickSort:
    """Test cases for quick sort implementation."""

    def test_empty_list(self):
        assert quick_sort([]) == []

    def test_single_element(self):
        assert quick_sort([42]) == [42]

    def test_two_elements_sorted(self):
        assert quick_sort([1, 2]) == [1, 2]

    def test_two_elements_unsorted(self):
        assert quick_sort([2, 1]) == [1, 2]

    def test_three_elements(self):
        assert quick_sort([3, 1, 2]) == [1, 2, 3]

    def test_already_sorted(self):
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_order(self):
        assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_with_duplicates(self):
        assert quick_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

    def test_all_same_elements(self):
        assert quick_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    def test_negative_numbers(self):
        assert quick_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_mixed_positive_negative(self):
        assert quick_sort([3, -2, 0, -8, 5, 1]) == [-8, -2, 0, 1, 3, 5]

    def test_large_numbers(self):
        assert quick_sort([1000000, 1, 500000, 999999]) == [
            1,
            500000,
            999999,
            1000000,
        ]

    def test_modifies_in_place(self):
        """Quick sort sorts in-place."""
        original = [3, 1, 2]
        result = quick_sort(original)
        assert result == [1, 2, 3]
        assert original == [1, 2, 3]

    def test_already_sorted_large(self):
        """Worst case for naive pivot selection."""
        arr = list(range(20))
        assert quick_sort(arr) == list(range(20))

    def test_many_duplicates(self):
        arr = [2, 1, 2, 1, 2, 1, 2, 1]
        assert quick_sort(arr) == [1, 1, 1, 1, 2, 2, 2, 2]
