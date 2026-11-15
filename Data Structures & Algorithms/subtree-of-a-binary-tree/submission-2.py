# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(s,t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return sameTree(s.left, t.left) and sameTree(s.right, t.right)

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if sameTree(node, subRoot):
                return True
        return False
            