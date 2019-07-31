
class TreeNode:
	def __init__(self, val):
		self.val = val 
		self.left, self.right = None, None
		
'''
Binary Tree problems can be solved by recursion of left and right tree.
Tree Traversal:
	DFS(preorder, 
		inorder,	==> stack LIFO
		postorder)
		
	BFS(level order)==> queue FIFO
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
		while stack or current:
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
			result.insert(0, level)
		
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
		
		
		
		
		
		
		
		
		
		
		
