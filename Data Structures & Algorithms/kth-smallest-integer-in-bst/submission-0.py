# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = -1
        def make_order(node):
            nonlocal count
            nonlocal res
            if not root:
                return
            if node.left:
                make_order(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            if node.right:
                make_order(node.right)
        
        make_order(root)
        return res

        