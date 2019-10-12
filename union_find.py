# Union find is a data structure which support two types of operations: Union and find, which both take O(1) in time complexity.

class UnionFind:
	
	def __init__(self, nodes):
		""""
		nodes: a list of nodes
		father: a hashmap to record the father of each node
		size: the number of the unions
		"""
		self.nodes = nodes
		self.father = {n:n for n in nodes}
		self.size = n
		
	def union(self, node1, node2):
		root1 = self.find(node1)
		root2 = self.find(node2)
		if root1 != root2:
			self.size -= 1
			self.father[root1] = root2
			
	def find(self, node):
		path = []
		while node != self.father[node]:
			path.append(node)
			node = self.father[node]
		
		for i in path:
			self.father[i] = node 
		
		return node 
		
