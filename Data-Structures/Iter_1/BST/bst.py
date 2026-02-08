from node import TreeNode


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
        self.root = None

    # ==================== INSERTION ====================

    def insert(self, val):
        self.root = self._insert_recursiver(self.root, val)

    def _insert_recursiver(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recursiver(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursiver(node.right, val)

        return node

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
        return self._search_recursiver(self.root, val)

    def _search_recursiver(self, node, val):
        if node is None:
            return None
        if val < node.val:
            return self._search_recursiver(node.left, val)
        elif val > node.val:
            return self._search_recursiver(node.right, val)

        return node

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
        return self.search(val) is not None

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
        if self.root is None:
            return self.root
        current = self.root
        while current.left is not None:
            current = current.left
        return current

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
        if self.root is None:
            return self.root
        current = self.root
        while current.right is not None:
            current = current.right
        return current

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
        self.root = self._delete_helper(self.root, val)

    def _delete_helper(self, node, val):
        # Base case: value not found
        if node is None:
            return None

        # Search for the node to delete
        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        else:
            # Found the node to delete!

            # Case 1: Leaf node (no children)
            if node.left is None and node.right is None:
                return None

            # Case 2a: Only right child
            if node.left is None:
                return node.right

            # Case 2b: Only left child
            if node.right is None:
                return node.left

            # Case 3: Two children
            # Find in-order successor (smallest in right subtree)
            successor = self._find_min_node(node.right)
            # Replace value with successor's value
            node.val = successor.val
            # Delete the successor from right subtree
            node.right = self._delete_helper(node.right, successor.val)

        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

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
        visited = []
        self._inorder_helper(self.root, visited)
        return visited

    def _inorder_helper(self, node, visited):
        if node is None:
            return
        self._inorder_helper(node.left, visited)
        visited.append(node.val)
        self._inorder_helper(node.right, visited)

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
        visited = []
        self._preorder_helper(self.root, visited)
        return visited

    def _preorder_helper(self, node, visited):
        if node is None:
            return
        visited.append(node.val)
        self._preorder_helper(node.left, visited)
        self._preorder_helper(node.right, visited)

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
        visited = []
        self._postorder_helper(self.root, visited)
        return visited

    def _postorder_helper(self, node, visited):
        if node is None:
            return
        self._postorder_helper(node.left, visited)
        self._postorder_helper(node.right, visited)
        visited.append(node.val)

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
        from collections import deque

        if self.root is None:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

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
        return self._height_helper(self.root)

    def _height_helper(self, node):
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return 1 + max(left_height, right_height)

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
        return self._count_nodes_helper(self.root)

    def _count_nodes_helper(self, node):
        if node is None:
            return 0
        return (
            1
            + self._count_nodes_helper(node.left)
            + self._count_nodes_helper(node.right)
        )

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
        return self._is_valid_bst_helper(self.root, None, None)

    def _is_valid_bst_helper(self, node, min_val, max_val):
        if node is None:
            return True

        if min_val is not None and node.val <= min_val:
            return False
        if max_val is not None and node.val >= max_val:
            return False

        return self._is_valid_bst_helper(
            node.left, min_val, node.val
        ) and self._is_valid_bst_helper(node.right, node.val, max_val)

    # ==================== UTILITY ====================

    def is_empty(self):
        """
        Check if tree is empty.

        Returns:
            bool: True if empty, False otherwise
        """
        return not self.root
