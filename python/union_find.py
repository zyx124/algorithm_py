'''
Union Find
Union Find is a data structure that provides union() and find() functions, both of which have the time complexity O(n).
This data structure is a direct graph in essence, each node of which has a Big Father. When doing the union() operation, we in fact union the Big Fathers.
'''

class UnionFind:
	
	def __init__(self, nodes):
		""""
		nodes: a list of nodes
		father: a hashmap to record the father of each node
		size: the number of the unions
		"""
		self.nodes = nodes
		self.father = {n: n for n in size}
		self.size = len(nodes)
		
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
		
		
#example Number of Islands II
"""
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

example:
Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        result = []
        self.num = 0
        self.father  = {}
        island = set()
        
        for o in operators:
            x, y = o.x, o.y
            if (x, y) in island:
                result.append(self.num)
                continue
            island.add((x, y))
            self.father[(x, y)] = (x, y)
            self.num += 1 
            for u, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x = x + u 
                new_y = y + v
                if (new_x, new_y) in island:
                    self.union((new_x, new_y), (x, y))
            result.append(self.num)
        
        return result
        
    def union(self, pa, pb):
        root_a = self.find(pa)
        root_b = self.find(pb)
        if root_b != root_a:
            self.father[root_a] = root_b
            self.num -= 1 
    
    def find(self, point):
        path = []
        while point != self.father[point]:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
            
        return point
            
