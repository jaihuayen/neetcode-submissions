# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        d = defaultdict(list)
        while q:
            node, l = q.popleft()
            d[l].append(node.val)
            if node.left:
                q.append((node.left, l + 1))
            if node.right:
                q.append((node.right, l + 1))
        return list(d.values())

            
