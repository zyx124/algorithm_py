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
		
	
