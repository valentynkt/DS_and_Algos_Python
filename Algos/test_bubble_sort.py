from bubble_sort import bubble_sort


class TestBubbleSort:
    """Test cases for bubble sort implementation."""

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([42]) == [42]

    def test_two_elements_sorted(self):
        assert bubble_sort([1, 2]) == [1, 2]

    def test_two_elements_unsorted(self):
        assert bubble_sort([2, 1]) == [1, 2]

    def test_already_sorted(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_order(self):
        assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_with_duplicates(self):
        assert bubble_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

    def test_all_same_elements(self):
        assert bubble_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    def test_negative_numbers(self):
        assert bubble_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_mixed_positive_negative(self):
        assert bubble_sort([3, -2, 0, -8, 5, 1]) == [-8, -2, 0, 1, 3, 5]

    def test_large_numbers(self):
        assert bubble_sort([1000000, 1, 500000, 999999]) == [1, 500000, 999999, 1000000]

    def test_modifies_in_place(self):
        """Bubble sort typically sorts in-place."""
        original = [3, 1, 2]
        result = bubble_sort(original)
        assert result == [1, 2, 3]
        # The original list should be modified
        assert original == [1, 2, 3]
