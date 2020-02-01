
class TreeNode:
	def __init__(self, val):
		self.val = val 
		self.left, self.right = None, None
		
'''
Most of Binary Tree problems can be solved by recursion of left and right tree.
First think about recursion on left and right subtrees.

Basic code problems:

1. Tree Traversal:
	DFS(preorder, 
		inorder,	==> stack LIFO
		postorder)
		
	BFS(level order)==> queue FIFO
2. Maximum Depth
3. Path Sum:
	- root to leaves
	- root to any node
	- any node to any node
	
	
Binary Search Tree(BST):
- left tree node value less than root value
- right tree node value larger than root value
- inorder traversal is a ascending sorted list

	
'''
		
## PREORDER traversal

## method 1 recursion 
class Solution:
	
	def preorderTraversal(self, root):
		self.result = []
		self.TraversalRoot(root)
		return self.result
		
	def TraversalRoot(self, root):
		if root is None:
			return 
		self.result.append(root.val)
		self.TraversalRoot(root.left)
		self.TraversalRoot(root.right)
		
## method 2 using stack
class Solution:
	
	def preorderTraversal(self, root):
		if root is None:
			return 
		stack = [root]
		while stack:
			node = stack.pop()
			result.append(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return result

# INORDER traversal

## method 1 recursion 
class Solution:
	
	def inorderTraversal(self, root):
		self.result = []
		self.TraversalRoot(root)
		return self.result
	
	def TraversalRoot(self, root):
		if root is None:
			return 
		self.TraversalRoot(root.left)
		self.result.append(root.val)
		self.TraversalRoot(root.right)
		

## method 2 traverse all the left node and then record and traverse the right node.
class Solution:
	
	def inorderTraversal(self, root):
		stack = []
		current = root
		result = []
		while current or stack: ## must check current first then stack
			if current:
				stack.append(current)
				current = current.left
			else:
				current = stack.pop()
				result.append(current.val)
				current = current.right
		return result
		
		
# POSTORDER 

## method 1: recursion
class Solution:
	
	def postorderTraversal(self, root):
		self.result = []
		self.TraversalRoot(root)
		return self.result
		
		
	def TraversalRoot(self, root):
		if root is None:
			return 
		self.TraversalRoot(root.left)
		self.TraversalRoot(root.right)
		self.result.append(root.val)
		
## method2: stack
class Solution:
	def postorderTraversal(self, root):
        
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
        

# Level Order Traversal: Using a queue to record the visited node

class Solution:
	
	def leverOrderTraversal(self, root):
		if not root:
			return []
		queue = [root]
		result = []
		
		while queue:
			level = []
			for i in range(len(queue))
				node = queue.pop(0)
				level.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			result.append(level)
		
		return result		
		

# DFS to traverse all the paths from root to leaves
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        
        result = []
        self.dfs(root, [str(root.val)], result)
        
        return result
    
    def dfs(self, root, path, result):
        
        if not root.left and not root.right:
            result.append('->'.join(path))
            return 
        
        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, path, result)
            path.pop()
            
        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, path, result)
            path.pop()
		
		
		
# Find Maximum depth of subtree 
class Solution:
	
	def maxDepth(self, root):
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Minimum depth of subtree 
class Solution:
	
	def minDepth(self, root):
		if not root:
			return 0
		left = self.minDepth(root.left)
		right = self.minDepth(root.right)
		if root.left and root.right:
			return min(left, right) + 1 
		else:
			return max(left, right) + 1
		
		
# Lowest common ancestors
class Solution:
	def lowestCommonAncestors(self, root, p, q):
		if not root:
			return root
		if root == p or root == q:
			return root
		left = self.lowestCommonAncestors(root.left, p, q)
		right = self.lowestCommonAncestors(root.right, p, q)
		
		if left and right:
			return root
		if left:
			return left
		if right:
			return right
			
			
 # Find all the root to leaf depth
 class Solution:
 	def root_to_leaf(self, root):
 		"""
 		return: all the paths from root to leaves
 		"""
 	
 		result = []
 		self.dfs(root, [root.val], result)
 		return result 
 		
 	def dfs(self, root, subset, result):
 		if not root.left and not root.right:
 			result.append(subset)
 		for node in [root.left, root.right]:
 			if node:
 				subset.append(node.val)
 				self.dfs(node, subset, result)
 				subset.pop()
 	
 # Maximum Path Sum (root to any)
 class Solution:
 	
 	def maximum_path_sum(self, root):
 		if not root:
	 		return 0
	 	left_sum = self.maximum_path_sum(root.left)
	 	right_sum = self.maximum_path_sum(root.right)
	 	
	 	return max(left_sum, right_sum, 0) + root.val 
 	
 	
 # Maximum Path Sum (any to any)
 class Solution
 	
 	 """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
    	self.max_path_sum = -sys.maxsize
    	self.helper(root):
    	
    	return self.max_path_sum
    
    def helper(self, root):
    	if not root:
    		return 0
    	left = self.helper(root.left)
    	if left < 0:
    		left = 0
    	right = self.helper(root.right)
    	if right < 0:
    		right = 0
    	self.max_path_sum = max(self.max_path_sum, left + right + root.val)
    	
    	return max(left + root.val, right + root.val)
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
		
		
		
