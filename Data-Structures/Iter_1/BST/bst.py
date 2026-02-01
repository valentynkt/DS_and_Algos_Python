

class BST:
    """
    Binary Search Tree implementation.

    BST Property:
        For every node N:
        - All values in N.left subtree < N.val
        - All values in N.right subtree > N.val

    Time Complexity (average / worst):
        - insert: O(log n) / O(n)
        - search: O(log n) / O(n)
        - delete: O(log n) / O(n)
        - min/max: O(log n) / O(n)

    Worst case occurs when tree becomes unbalanced (like a linked list).
    """

    def __init__(self):
        """
        Initialize an empty BST.

        Attributes:
            - root: Reference to the root node (None if empty)
        """
        # TODO: Initialize root
        pass

    # ==================== INSERTION ====================

    def insert(self, val):
        """
        Insert a value into the BST.

        Args:
            val: The value to insert

        Returns:
            None

        Time Complexity: O(log n) average, O(n) worst

        Algorithm:
            1. If tree is empty, create root
            2. Otherwise, compare val with current node:
               - If val < current: go left
               - If val > current: go right
            3. Repeat until you find an empty spot
            4. Insert new node there

        Can be implemented iteratively or recursively.
        Recursive is more elegant, iterative uses less stack space.

        Visual example - insert 5:
            Before:       After:
                8            8
               / \          / \
              3   10       3   10
             /            / \
            1            1   5
        """
        # TODO: Implement (try both recursive and iterative)
        pass

    # ==================== SEARCH ====================

    def search(self, val):
        """
        Search for a value in the BST.

        Args:
            val: The value to find

        Returns:
            TreeNode if found, None otherwise

        Time Complexity: O(log n) average, O(n) worst

        Algorithm:
            1. Start at root
            2. Compare val with current node:
               - If equal: found it!
               - If val < current: go left
               - If val > current: go right
            3. If you hit None, value doesn't exist

        This is essentially binary search on a tree structure.
        Each comparison eliminates half the remaining nodes (when balanced).
        """
        # TODO: Implement
        pass

    def contains(self, val):
        """
        Check if value exists in the BST.

        Args:
            val: The value to check

        Returns:
            bool: True if exists, False otherwise

        Time Complexity: O(log n) average, O(n) worst

        Implementation:
            Simply wrap search() and check if result is not None.
        """
        # TODO: Implement
        pass

    # ==================== MIN / MAX ====================

    def find_min(self):
        """
        Find the minimum value in the BST.

        Returns:
            The minimum value, or None if tree is empty

        Time Complexity: O(log n) average, O(n) worst

        Algorithm:
            Keep going LEFT until you can't anymore.
            The leftmost node is the minimum.

        Visual:
                8
               / \
              3   10
             /
            1  <-- minimum (leftmost)
        """
        # TODO: Implement
        pass

    def find_max(self):
        """
        Find the maximum value in the BST.

        Returns:
            The maximum value, or None if tree is empty

        Time Complexity: O(log n) average, O(n) worst

        Algorithm:
            Keep going RIGHT until you can't anymore.
            The rightmost node is the maximum.
        """
        # TODO: Implement
        pass

    # ==================== DELETION ====================

    def delete(self, val):
        """
        Delete a value from the BST.

        Args:
            val: The value to delete

        Returns:
            bool: True if deleted, False if not found

        Time Complexity: O(log n) average, O(n) worst

        THIS IS THE HARDEST OPERATION. Three cases:

        Case 1: Node has NO children (leaf)
            Simply remove it.

            Before:     After:
               5          5
              / \        /
             3   7      3
                  \
                   9

            Delete 7 (leaf) -> just remove

        Case 2: Node has ONE child
            Replace node with its child.

            Before:     After:
               5          5
              / \        / \
             3   7      3   9
                  \
                   9

            Delete 7 (one child) -> replace with 9

        Case 3: Node has TWO children
            Find the in-order successor (smallest in right subtree)
            OR in-order predecessor (largest in left subtree).
            Replace node's value with successor's value.
            Delete the successor (which has at most one child).

            Before:     After:
               5          6
              / \        / \
             3   8      3   8
                / \        / \
               6   9      7   9
                \
                 7

            Delete 5 -> replace with 6 (successor), delete original 6

        Hint: Recursive approach is cleaner. The function returns
        the new subtree root after deletion.
        """
        # TODO: Implement
        pass

    # ==================== TRAVERSALS ====================
    # These visit every node in a specific order.
    # Understanding traversals is KEY to understanding trees.

    def inorder(self):
        """
        In-order traversal: Left -> Node -> Right

        Returns:
            list: Values in sorted ascending order

        Time Complexity: O(n)

        For a BST, in-order traversal gives you SORTED output!
        This is a key property of BSTs.

        Example:
                4
               / \
              2   6
             / \ / \
            1  3 5  7

        In-order: [1, 2, 3, 4, 5, 6, 7]

        Algorithm (recursive):
            1. Traverse left subtree
            2. Visit current node
            3. Traverse right subtree
        """
        # TODO: Implement
        pass

    def preorder(self):
        """
        Pre-order traversal: Node -> Left -> Right

        Returns:
            list: Values in pre-order

        Time Complexity: O(n)

        Use case: Creating a copy of the tree.
        If you insert values in pre-order into an empty BST,
        you get the exact same tree structure.

        Example:
                4
               / \
              2   6
             / \ / \
            1  3 5  7

        Pre-order: [4, 2, 1, 3, 6, 5, 7]

        Algorithm (recursive):
            1. Visit current node
            2. Traverse left subtree
            3. Traverse right subtree
        """
        # TODO: Implement
        pass

    def postorder(self):
        """
        Post-order traversal: Left -> Right -> Node

        Returns:
            list: Values in post-order

        Time Complexity: O(n)

        Use case: Deleting/freeing a tree.
        You must delete children before deleting the parent.

        Example:
                4
               / \
              2   6
             / \ / \
            1  3 5  7

        Post-order: [1, 3, 2, 5, 7, 6, 4]

        Algorithm (recursive):
            1. Traverse left subtree
            2. Traverse right subtree
            3. Visit current node
        """
        # TODO: Implement
        pass

    def level_order(self):
        """
        Level-order traversal: Level by level, left to right.
        Also known as Breadth-First Search (BFS).

        Returns:
            list: Values level by level

        Time Complexity: O(n)

        Example:
                4
               / \
              2   6
             / \ / \
            1  3 5  7

        Level-order: [4, 2, 6, 1, 3, 5, 7]

        Algorithm:
            Use a QUEUE (not recursion).
            1. Enqueue root
            2. While queue not empty:
               a. Dequeue node
               b. Visit it
               c. Enqueue its children (left, then right)

        This is where your Queue implementation comes in handy!
        """
        # TODO: Implement
        pass

    # ==================== TREE PROPERTIES ====================

    def height(self):
        """
        Calculate the height of the tree.

        Returns:
            int: Height (number of edges on longest path from root to leaf)
                 Returns -1 for empty tree (convention)

        Time Complexity: O(n)

        Examples:
            Empty tree: height = -1
            Single node: height = 0
            Root with one child: height = 1

                4          height = 2
               / \
              2   6
             /
            1

        Algorithm (recursive):
            height(node) = 1 + max(height(left), height(right))
            Base case: empty node returns -1
        """
        # TODO: Implement
        pass

    def count_nodes(self):
        """
        Count total nodes in the tree.

        Returns:
            int: Number of nodes

        Time Complexity: O(n)

        Algorithm (recursive):
            count(node) = 1 + count(left) + count(right)
            Base case: empty node returns 0
        """
        # TODO: Implement
        pass

    def is_valid_bst(self):
        """
        Validate that this tree satisfies the BST property.

        Returns:
            bool: True if valid BST, False otherwise

        Time Complexity: O(n)

        Common mistake: Only checking node > left and node < right.
        This fails for:
                5
               / \
              3   8
               \
                7  <-- Invalid! 7 > 5 but it's in left subtree

        Correct approach: Pass down min/max bounds.
        Each node must be within (min, max) range.
        Going left: update max = current value
        Going right: update min = current value
        """
        # TODO: Implement
        pass

    # ==================== UTILITY ====================

    def is_empty(self):
        """
        Check if tree is empty.

        Returns:
            bool: True if empty, False otherwise
        """
        # TODO: Implement
        pass

    def __str__(self):
        """
        String representation for debugging.
        Shows in-order traversal (sorted values).
        """
        # TODO: Implement (optional)
        pass
