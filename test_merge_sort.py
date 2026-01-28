from merge_sort import merge, merge_sort


class TestMerge:
    """Test cases for the merge helper function."""

    def test_merge_empty_lists(self):
        assert merge([], []) == []

    def test_merge_left_empty(self):
        assert merge([], [1, 2, 3]) == [1, 2, 3]

    def test_merge_right_empty(self):
        assert merge([1, 2, 3], []) == [1, 2, 3]

    def test_merge_single_elements(self):
        assert merge([1], [2]) == [1, 2]

    def test_merge_single_elements_reversed(self):
        assert merge([2], [1]) == [1, 2]

    def test_merge_interleaved(self):
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_left_all_smaller(self):
        assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_right_all_smaller(self):
        assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]

    def test_merge_with_duplicates(self):
        assert merge([1, 3, 3], [2, 3, 4]) == [1, 2, 3, 3, 3, 4]

    def test_merge_unequal_lengths(self):
        assert merge([1, 5], [2, 3, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


class TestMergeSort:
    """Test cases for merge sort implementation."""

    def test_empty_list(self):
        assert merge_sort([]) == []

    def test_single_element(self):
        assert merge_sort([42]) == [42]

    def test_two_elements_sorted(self):
        assert merge_sort([1, 2]) == [1, 2]

    def test_two_elements_unsorted(self):
        assert merge_sort([2, 1]) == [1, 2]

    def test_three_elements(self):
        assert merge_sort([3, 1, 2]) == [1, 2, 3]

    def test_already_sorted(self):
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_order(self):
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_with_duplicates(self):
        assert merge_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

    def test_all_same_elements(self):
        assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    def test_negative_numbers(self):
        assert merge_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_mixed_positive_negative(self):
        assert merge_sort([3, -2, 0, -8, 5, 1]) == [-8, -2, 0, 1, 3, 5]

    def test_power_of_two_length(self):
        """Arrays with 2^n length divide evenly."""
        assert merge_sort([8, 4, 2, 1, 7, 3, 6, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_non_power_of_two_length(self):
        """Arrays with non-2^n length have unequal splits."""
        assert merge_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]

    def test_does_not_modify_original(self):
        """Merge sort typically returns a new list."""
        original = [3, 1, 2]
        result = merge_sort(original)
        assert result == [1, 2, 3]
        assert original == [3, 1, 2]  # Original unchanged
