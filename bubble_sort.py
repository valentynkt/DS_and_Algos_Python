def bubble_sort(arr: list) -> list:
    """
    Sort the array in ascending order using bubble sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        The sorted list (sorted in-place, but also returned)
    """
    # YOUR IMPLEMENTATION HERE
    swapping = True
    end = len(arr)
    while swapping:
        swapping = False
        for i in range(1, end):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapping = True
        end -= 1
    return arr
