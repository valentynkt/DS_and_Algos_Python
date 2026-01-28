def partition(arr: list, low: int, high: int) -> int:
    """
    Partition the array around a pivot element.

    Rearranges elements so that all elements less than or equal to the pivot
    are to its left, and all elements greater are to its right.

    Args:
        arr: List of comparable elements
        low: Starting index of the partition range
        high: Ending index of the partition range (inclusive, used as pivot)

    Returns:
        The final index of the pivot element after partitioning
    """
    # YOUR IMPLEMENTATION HERE
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list, low: int = 0, high: int | None = None):
    """
    Sort the array in ascending order using quick sort algorithm (recursive, in-place).

    Args:
        arr: List of comparable elements
        low: Starting index (default 0)
        high: Ending index inclusive (default last index)

    Returns:
        The sorted list (sorted in-place, but also returned)
    """
    if high is None:
        high = len(arr) - 1
    # YOUR IMPLEMENTATION HERE
    if low < high:
        middle = partition(arr, low, high)
        quick_sort(arr, low, middle - 1)
        quick_sort(arr, middle + 1, high)
    return arr
