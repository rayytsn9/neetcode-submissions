# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # same if equal node values and same structure
        # 
        # Potential approach:
        # post order tree traversal -> 2 lists -> compare

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        left_status = self.isSameTree(p.left, q.left)
        right_status = self.isSameTree(p.right, q.right)

        return True if left_status == right_status and left_status else False

        






