'''
Array is similar to linked lists.
The problems and techniques that relate to array:
- Sort 
- Merge
- Median --> find Kth element
- Subarray --> prefix sum
- Two Pointers
'''

# Merge two Sorted array (same method as merging two sorted linked lists)
class Solution:
	
	def mergeSortedArray(self, A, B):
		result = []
		i, j = 0, 0
		while i < len(A) and j < len(B):
			if A[i] <= B[j]:
				result.append(A[i])
				i += 1
			else:
				result.append(B[j])
				j += 1
		while i < len(A):
			result.append(A[i])
			i += 1
		while j < len(B):
			result.append(B[j])
			j += 1
			
		return result
		
# Median of Two Sorted Arrays --> find Kth element
class Solution:
	
	def medianTwoArrays(self, A, B):
		n = len(A) + len(B)
		if n % 2 != 0:
			return self.findKth(A, B, n // 2 + 1)
		else:
			x = self.findKth(A, B, n // 2)
			y = self.findKth(A, B, n // 2 + 1)
			return (x + y) / 2
			
	def findKth(self, A, B, k):
		if len(A) == 0:
			return B[k - 1]
		if len(B) == 0:
			return A[k - 1]
		if k == 1:
			return min(A[0], B[0])

		mid_a = A[k // 2 - 1] if len(A) >= k // 2 else sys.maxsize
		mid_b = B[k // 2 - 1] if len(B) >= k // 2 else sys.maxsize
		
		if mid_a > mid_b:
			return self.findKth(A, B[k // 2:], k - k // 2)
		else:
			return self.findKth(A[k // 2:], B, k - k // 2)
			
			
