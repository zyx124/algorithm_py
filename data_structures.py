'''
Linear Data Structure:
- Queue FIFO	--> BFS
- Stack LIFO	--> DFS
- Hash

Advanced use of stacks: monotune stacks
to find first element larger/smaller than the element in the stack.

Tree Data Structure:
- Heap/Priority Queue	--> sort
- TreeMap
- Trie
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
Heap:
Heap is a tree data structure, which has push(), pop(), peak() methods. Push(), pop() are both O(logn) and peak() is O(1).

It also has remove() operation to delete an arbitrary node in the heap. If we remove a node with, we can use Hashheap to reduce the time complexity from O(n) to O(logn). The key in the hash is the node value and the value is the node's index.

For a heap, a node with index i has left son with index 2 * i + 1, right son with index 2 * i + 2, the parent has index (i - 1) // 2.

The basic for a min heap is that the left and the right children must be larger than their parent.

Basic operations of a heap that needs to know:
- delete a node: if the node is a leaf, just delete it. If it is not a leaf, replace it with the last leaf of its children, and then sift down until the heap is valid.
- add a node: Add it to the leaf, then sift up until the heap is valid.
- heapify: If using sift up just like adding a node, it will take O(nlogn) to finish, where logn is the height of the tree. To reduce the time complexity, we sift down instead of sift up, which will take O(n). Let h=logn be the height of the tree, and k is the layer number from bottom, kth layer will have 2^(h - k) nodes, and each node will sift down at most k times. We have sum(k * 2^(h - k)) for k from 1 to h, we can simplify the equation as sum((k/2^k) * 2^h), we know sum of k/2^k will be bounded to a constant and 2^h = n. The total time is thus O(n).

In python, heapq is the lib to realize a min heap. heap.pop() or heap[0] will return the smallest element in the heap.

'''
 
# An example of heapify
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A) // 2, -1, -1):
            self.sift_down(A, i)
            
    def sift_down(self, A, i):
        n = len(A)
        while i < n:
            minId = i 
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and A[left] < A[minId]:
                minId = left
            if right < n and A[right] < A[minId]:
                minId = right
            if minId == i:
                break
            A[i], A[minId] = A[minId], A[i]
            
            i = minId


# Python heapq does not support hashheap where remove a node takes O(logn). We need to implement it by ourselves. We map the node to its index in the heap so that we can find it using O(1) and then by sift_down which takes O(logn), we get the remove() operation with O(logn). 

class HashHeap:
	"""
	The remove operation is O(nlogn)
	"""
	def __init__(self, desc=False):
		self.hash = dict()
		self.heap = []
		self.desc = desc
	
	@property
	def size(self):
		return len(self.heap)
		
	def push(self, item):
		self.heap.append(item)
		self.hash[item] = self.size - 1
		self._sift_up(self.size - 1)
																																																																							
	def pop(self):
		item = self.heap[0]
		self.remove(item)
		return item
	
	def top(self):
		return self.heap[0]
		
	def remove(self, item):
		if item not in self.hash:
			return
		index = self.hash[item]
		self._swap(index, self.size - 1)
		
		del self.hash(item)
		self.heap.pop()
		
		if index < self.size:
			self._sift_up(index)
			self.sift_down(index)
	
	def _smaller(self, left, right):
		return right < left if self.desc else left < right
	
	def _sift_up(self, index):
		while index != 0:
			parent = index // 2
			if self._smaller(self.heap[parent], self.heap[index]):
				break
			self._swap(parent, index)
			index = parent
			
	def _sift_down(self, index):
		if indx is None:
			return 
		while index * 2 < self.size:
			smallest = index
			left = index * 2
			right = index * 2 + 1
			
			if self._smaller(self.heap[left], self.heap[smallest]):
				smallest = index
			
			if right < self.size and self._smaller(self.heap[right], self[smallest]):
				smallest = index
			
			if smallest == index:
				break
		
			self._swap(index, smallest)
			index = smallest
	
	def _swap(self, i, j):
		ele1 = self.heap[i]
		ele2 = self.heap[j]
		self.heap[i] = ele2
		self.heap[j] = ele2
		self.hash[ele1] = j
		self.hash[ele2] = i
		

## Example: Sliding Window
"""
The basic idea is that by maintaining two heaps, we let the median in the top of the heaps. The maximum number of the maxheap is less than the minimum number of the minheap. 
To keep the sliding window in the predifined length, remove method is needed. If we use the sift_down method of the heaps, the total time is O(nklogk) where k is the length of the sliding window. If we define the remove method as above, which takes O(logk), we can reduce the time to O(nlogk).
"""

import heapq
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        self.maxheap = []
        self.minheap = []
        result = []
        
        for i in range(len(nums)):
            if len(self.maxheap) == 0 or nums[i] <= -self.maxheap[0]:
                heapq.heappush(self.maxheap, -nums[i])
            else:
                heapq.heappush(self.minheap, nums[i])
            
            self.balance()
            if i >= k:
                if nums[i - k] >= self.minheap[0]:
                    self.minheap.remove(nums[i - k])
                    heapq.heapify(self.minheap)
                else:
                    self.maxheap.remove(-nums[i - k])
                    heapq.heapify(self.maxheap)
            
                self.balance()
            
            if i >= k - 1:
                result.append(-self.maxheap[0])
                
        return result
                
    
    def balance(self):
        while len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        while len(self.minheap) < len(self.maxheap) - 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            

# implement a Trie
"""
Trie is a data structure that stores strings, which can save space because several words with the same prefix can share the path of the prefix.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_valid = False
        
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_valid = True

    def find(self, word):
        node = self.root
        for i in word:
            node = node.children.get(i)
            if not node:
                return None
        return node
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and n
        ode.is_valid
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None

