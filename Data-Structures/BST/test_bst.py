from node import BSTNode


def build_tree(values):
    """Helper to build a BST from a list of values."""
    if not values:
        return None
    root = BSTNode(values[0])
    for val in values[1:]:
        root.insert(val)
    return root


def tree_to_list(node):
    """In-order traversal to list (should be sorted for valid BST)."""
    if node is None or node.val is None:
        return []
    return tree_to_list(node.left) + [node.val] + tree_to_list(node.right)


# Delete leaf node
def test_delete_leaf():
    root = build_tree([10, 5, 15, 3])
    #       10
    #      /  \
    #     5    15
    #    /
    #   3
    root = root.delete(3)
    assert tree_to_list(root) == [5, 10, 15]


# Delete node with only left child
def test_delete_one_child_left():
    root = build_tree([10, 5, 15, 3])
    root = root.delete(5)
    assert tree_to_list(root) == [3, 10, 15]


# Delete node with only right child
def test_delete_one_child_right():
    root = build_tree([10, 5, 15, 20])
    #       10
    #      /  \
    #     5    15
    #            \
    #             20
    root = root.delete(15)
    assert tree_to_list(root) == [5, 10, 20]


# Delete node with two children
def test_delete_two_children():
    root = build_tree([10, 5, 15, 3, 7, 12, 20])
    #        10
    #       /  \
    #      5    15
    #     / \   / \
    #    3   7 12  20
    root = root.delete(5)
    # Successor of 5 is 7
    assert tree_to_list(root) == [3, 7, 10, 12, 15, 20]


# Delete root with two children
def test_delete_root():
    root = build_tree([10, 5, 15, 3, 12, 20])
    root = root.delete(10)
    # Successor of 10 is 12
    assert tree_to_list(root) == [3, 5, 12, 15, 20]


# Delete value not in tree
def test_delete_nonexistent():
    root = build_tree([10, 5, 15])
    root = root.delete(99)
    assert tree_to_list(root) == [5, 10, 15]


if __name__ == "__main__":
    test_delete_leaf()
    test_delete_one_child_left()
    test_delete_one_child_right()
    test_delete_two_children()
    test_delete_root()
    test_delete_nonexistent()
    print("All tests passed!")
