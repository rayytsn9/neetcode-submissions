# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
    # strategy:
    # implement isSameTree as a lambda function
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            # same if equal node values and same structure
            # 
            # Potential approach:
            # post order tree traversal -> 2 lists -> compare
            # on second thought since isSameTree returns bool, 
            # then, recursively check left and right subtrees 
            # are equal in value and structure

            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            left_status = isSameTree(p.left, q.left)
            right_status = isSameTree(p.right, q.right)

            return left_status and right_status

        if not subRoot:
            return True

        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
