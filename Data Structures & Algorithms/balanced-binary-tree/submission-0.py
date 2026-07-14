# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        bf = {}

        def node_balance(node):
            if not node:
                return -1

            leftHeight = node_balance(node.left)
            rightHeight = node_balance(node.right)

            balance = rightHeight - leftHeight
            bf[node] = balance

            return 1 + max(leftHeight, rightHeight)

        valid = [-1,0,1]

        node_balance(root)

        for node in bf:
            if bf[node] not in valid:
                return False
        
        return True
                