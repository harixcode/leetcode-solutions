#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depth = 1
    if root == None:
        return 0
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return 1 + max(left_depth,right_depth)
    
