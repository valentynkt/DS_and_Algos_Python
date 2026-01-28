def merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left: First sorted list
        right: Second sorted list

    Returns:
        A new sorted list containing all elements from both lists
    """

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr: list) -> list:
    """
    Sort the array using merge sort algorithm (recursive).

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list
    """
    if len(arr) < 2:
        return arr
    list_len = len(arr)
    left_side = merge_sort(arr[: list_len // 2])
    right_side = merge_sort(arr[list_len // 2 :])
    # YOUR IMPLEMENTATION HERE
    return merge(left_side, right_side)
