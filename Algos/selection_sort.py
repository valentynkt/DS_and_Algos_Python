def selection_sort(arr: list) -> list:
    """
    Sort the array in ascending order using selection sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        The sorted list (sorted in-place, but also returned)
    """
    # YOUR IMPLEMENTATION HERE
    for i in range(0, len(arr)):
        smallest_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_idx]:
                arr[j], arr[smallest_idx] = arr[smallest_idx], arr[j]
        arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]
    return arr
