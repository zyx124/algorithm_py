'''
Linear Data Structure:
- Queue FIFO	--> BFS
- Stack LIFO	--> DFS
- Hash

Tree Data Structure:
- Heap/Priority Queue	--> sort
- TreeMap
'''

# top K largest number
# heappop method will pop the smallest number in the heap. If we want to pop the largest number, we need to push into the heap with opposite sign of the numbers.
from heapq import heappush, heappop
class Solution:
	
	def __init__(self, k)
		self.k = k
		self.heap = []
		
	def add(self, num):
		heappush(self.heap, num)
		if len(self.heap) > self.k:
			heappop(self.heap)
			
	def topk(self):
		return sorted(self.heap, reverse=True)
		

'''
For a heap, a node with index i has left son with index 2 * i + 1, right son with index 2 * i + 2, the parent has index (i - 1) // 2.

The basic for a min heap is that the left and the right children must be larger than their parent.

Basic operations of a heap that needs to know:
- delete a node: if the node is a leaf, just delete it. If it is not a leaf, replace it with the last leaf of its children, and then sift down until the heap is valid.
- add a node: Add it to the leaf, then sift up until the heap is valid.
- heapify: If using sift up just like adding a node, it will take O(nlogn) to finish, where logn is the height of the tree. To reduce the time complexity, we sift down instead of sift up, which will take O(n). Let h=logn be the height of the tree, and k is the layer number from bottom, kth layer will have 2^(h - k) nodes, and each node will sift down at most k times. We have sum(k * 2^(h - k)) for k from 1 to h, we can simplify the equation as sum((k/2^k) * 2^h), we know sum of k/2^k will be bounded to a constant and 2^h = n. The total time is thus O(n).
'''

