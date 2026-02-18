# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


from operator import index
from typing import Any, Optional


class Codec:
    def __init__(self) -> None:
        self.index = 0

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        return ",".join(str(node) for node in self.preorder(root))

    def preorder(self, root: TreeNode | None) -> list[Any]:
        return self._preorder_helper(root, [])

    def _preorder_helper(self, node: TreeNode | None, visited) -> list[Any]:
        if node is None:
            visited.append(None)
            return visited
        visited.append(node.val)
        self._preorder_helper(node.left, visited)
        self._preorder_helper(node.right, visited)
        return visited

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        self.index = 0
        input = data.split(",")
        return self._deserialize_helper(input)

    def _deserialize_helper(self, input_arr: list[str]):
        if input_arr[self.index] == "None":
            self.index += 1
            return None
        node = TreeNode(int(input_arr[self.index]))
        self.index += 1
        node.left = self._deserialize_helper(input_arr)
        node.right = self._deserialize_helper(input_arr)
        return node
