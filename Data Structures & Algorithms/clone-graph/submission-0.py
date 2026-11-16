"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copy = {}
        copy[node] = Node(node.val)
        q = deque([node])

        while q:
            sub_node = q.popleft()
            for n in sub_node.neighbors:
                if n not in copy:
                    copy[n] = Node(n.val)
                    q.append(n)
                copy[sub_node].neighbors.append(copy[n])
        return copy[node]
                
            