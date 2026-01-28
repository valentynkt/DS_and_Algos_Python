from selection_sort import selection_sort


class TestSelectionSort:
    """Test cases for selection sort implementation."""

    def test_empty_list(self):
        assert selection_sort([]) == []

    def test_single_element(self):
        assert selection_sort([42]) == [42]

    def test_two_elements_sorted(self):
        assert selection_sort([1, 2]) == [1, 2]

    def test_two_elements_unsorted(self):
        assert selection_sort([2, 1]) == [1, 2]

    def test_three_elements_reverse(self):
        assert selection_sort([3, 2, 1]) == [1, 2, 3]

    def test_already_sorted(self):
        assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_order(self):
        assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_with_duplicates(self):
        assert selection_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

    def test_all_same_elements(self):
        assert selection_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    def test_negative_numbers(self):
        assert selection_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_mixed_positive_negative(self):
        assert selection_sort([3, -2, 0, -8, 5, 1]) == [-8, -2, 0, 1, 3, 5]

    def test_large_numbers(self):
        assert selection_sort([1000000, 1, 500000, 999999]) == [
            1,
            500000,
            999999,
            1000000,
        ]

    def test_minimum_at_end(self):
        """Minimum must travel from the end to position 0."""
        assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_minimum_already_in_place(self):
        """First element is already the minimum."""
        assert selection_sort([1, 5, 3, 4, 2]) == [1, 2, 3, 4, 5]

    def test_modifies_in_place(self):
        """Selection sort sorts in-place."""
        original = [3, 1, 2]
        result = selection_sort(original)
        assert result == [1, 2, 3]
        assert original == [1, 2, 3]
