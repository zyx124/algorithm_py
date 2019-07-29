'''
Array is similar to linked lists.
The problems and techniques that relate to array:
- Sort 
- Merge
- Median --> find Kth element
- Subarray --> prefix sum
- Two Pointers (sort first)
'''

# Merge two Sorted arrays (same method as merging two sorted linked lists)
# --> merge K sorted arrays
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

# Maximum subarray  
class Solution:
	
	## Prefix Sum
	def maxSubArray(self, nums):
		min_sum, max_sum = 0, -sys.maxsize
		prefix_sum = 0
		
		for n in nums:
			prefix_sum += n
			max_sum = max(max_sum, prefix_sum - min_sum)
			min_sum = min(min_sum, prefix_sum)
			
		return max_sum
		
	## Kadane's method: use an array to keep track of the value of the maximum subarray  
	## which containing the current coorsponding position of the original array. 
	## It is a dynamic programming method. 
	def maxSubArray(self, nums):
		m = nums
		for i in range(1, len(nums)):
			m[i] = max(nums[i], m[i - 1] + nums[i])
		
		return max(m)
		
	
# Two Sum: find the index of 2 numbers in an array that sum up to the target  --> hash/two pointers

# Three sum  can be translated into several two-sum problems.
class Solution:
	
	## Hash Table
	def TwoSum(self, numbers, target):
		record = {}
		for i in range(len(numbers)):
			if target - numbers[i] in hash:
				return [record[target - numbers[i]], i]
			record[numbers[i]] = i
		return [-1, -1]
		
	## two pointers
	def TwoSum(self, numbers, target):
		index_table = [i for i, v in sorted(enumerate(numbers), key=lambda x:x[1])]
		numbers.sort()
		left, right = 0, len(numbers) - 1
		while left <= right:
			if numbers[left] + numbers[right] == target:
				return sorted([index_table[left], index_table[right]])
			elif numbers[left] + numbers[right] < target:
				left += 1
			else:
				right -= 1
		return [-1 -1]

# Partition an array
class Solution:
	
	def partitionArray(self, nums, k):
		start = 0
		for i in range(len(nums)):
			if nums[i] < k:
				nums[i], nums[start] = nums[start], nums[i]
				start += 1
				
		return start


			
