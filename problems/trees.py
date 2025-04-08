from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def bfs(root):
    q = [root]
    while q:
        node = q.pop(0)
        print(node.val)
        q.append(node.left)
        q.append(node.right)
    return

# https://leetcode.com/problems/invert-binary-tree/
def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    if not root.left and not root.right:
        return root

    tmp = root.left.val
    root.left.val = root.right.val
    root.right.val = tmp

    self.invert_tree(root.left)
    self.invert_tree(root.right)

    return root

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
def max_depth_iterative(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = [(root, 1)]
    visited = set()
    max_level = 1
    while q:
        node, level = q.pop(0)
        visited.add(node)
        if level > max_level:
            max_level = level

        if node.left and node.left not in visited:
            q.append((node.left, level+1))

        if node.right and node.right not in visited:
            q.append((node.right, level+1))
    return max_level

# https://leetcode.com/problems/same-tree/
def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif p and not q:
        return False
    elif not p and q:
        return False
    else:
        if p.val != q.val:
            return False
    return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

# https://leetcode.com/problems/subtree-of-another-tree/
def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if not sub_root:
        return True
    if not root:
        return False
    if self.is_same_tree(root, sub_root):
        return True

    return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

# root is a binary search tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
def lowest_common_ancestor(self, root: TreeNode, p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
    if p.val <= root.val <= q.val:
        return root
    if q.val <= root.val <= p.val:
        return root

    if p.val < root.val and q.val < root.val:
        return self.lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return self.lowest_common_ancestor(root.right, p, q)

    # iterative solution
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr

# https://leetcode.com/problems/binary-tree-level-order-traversal/
def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = [root]
    levels = []
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)

            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(level)
    return levels

# https://leetcode.com/problems/validate-binary-search-tree/
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def is_valid(node, floor, ceiling) -> bool:
        if not node:
            return True
        if node.left and node.left.val > ceiling:
            return False
        if node.right and node.right.val < floor:
            return False
        return is_valid(node.left) and is_valid(node.right)
    return is_valid(root, float("-inf"), float("inf"))

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def inorder(node):
        if not node:
            return []

        return inorder(node.left) + [node.val] + inorder(node.right)

    return inorder(root)[k - 1]

def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
    # go as far left as possible, then pop the stack and append right child
    i = 1
    stack = [root]
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if i == k:
            return curr.val
        i += 1
        curr = curr.right

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    # i = 0
    # while inorder[i] != preorder[0] and i < len(inorder) - 1:
    #     i += 1
    i = inorder.index(preorder[0])

    root.left = self.buildTree(preorder[1:1 + i], inorder[:i])
    root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])

    return root

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    """
    :type root: TreeNode
    :rtype: int
    """

    self.res = root.val

    self.dfsMaxPathSum(root)

    return self.res

def dfsMaxPathSum(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    # calculate local max
    left_max = self.dfsMaxPathSum(root.left)
    right_max = self.dfsMaxPathSum(root.right)

    local_max = root.val
    if left_max > 0:
        local_max += left_max
    if right_max > 0:
        local_max += right_max
    self.res = max(self.res, local_max)

    # return max without splitting
    return root.val + max(left_max, right_max, 0)


# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class Codec:
def serializeBFS(self, root: TreeNode) -> str:
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return "[]"

    bfs = []
    q = [root]

    while q:
        node = q.pop(0)
        if node:
            bfs.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            bfs.append(None)

    return str(bfs)

def deserializeBFS(self, data: str) -> Optional[TreeNode]:
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data == "[]":
        return None

    enc = data.strip("[]").split(", ")
    root = TreeNode(int(enc[0]))
    q = [root]

    i = 1
    while i < len(enc) - 1:
        x = enc[i]
        parent = q.pop(0)
        if x != "None":
            parent.left = TreeNode(int(x))
            q.append(parent.left)
        y = enc[i + 1]
        if y != "None":
            parent.right = TreeNode(int(y))
            q.append(parent.right)
        i += 2

    return root

def serializeDFS(self, root: TreeNode) -> str:
    enc = []

    def preorder(root):
        if not root:
            enc.append("N")
            return
        enc.append(str(root.val))
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return ",".join(enc)

def deserializeDFS(self, data: str) -> TreeNode:
    vals = iter(data.split(","))

    def decode():
        val = next(vals)
        if val == 'N':
            return None
        node = TreeNode(int(val))
        node.left = decode()
        node.right = decode()
        return node

    return decode()