
class TreeNode:
	def __init__(self, val):
		self.val = val 
		self.left, self.right = None, None
		
## PREORDER traversal

# method 1 recursion 
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
		
# method 2 using stack
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

## INORDER traversal

# method 1 recursion 
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
		

# method 2 traverse all the left node and then record and traverse the right node.
class Solution:
	
	def inorderTraversal(self, root):
		stack = []
		current = root
		result = []
		while stack or current:
			if current:
				stack.append(current)
				current = current.left
			else:
				current = stack.pop()
				result.append(current.val)
				current = current.right
		return result
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
