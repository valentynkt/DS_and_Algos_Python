def insertion_sort(arr: list) -> list:
    """
    Sort the array in ascending order using insertion sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        The sorted list (sorted in-place, but also returned)
    """
    # YOUR IMPLEMENTATION HERE
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr
