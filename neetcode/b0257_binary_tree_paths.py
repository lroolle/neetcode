""" 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

     1
   /   \
  2     3
 / \
4   5

All root-to-leaf paths are:

["1->2->4", "1->2->5", "1->3"]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_tree_paths(root):
    ret = list()
    if not root:
        return []
    if (root.left is None and root.right is None):
        return [str(root.val)]
    full_tree = binary_tree_paths(root.left) + \
            binary_tree_paths(root.right)
    for leaf in full_tree:
        ret.append(str(root.val) + '->' + leaf)
    return ret


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.right = node3
root.left = node2
node2.right = node5
node2.left = node4


if __name__ == '__main__':
    print(binary_tree_paths(root))

