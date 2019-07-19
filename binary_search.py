#! /usr/lib/python

## binary search a number 
def binary_search(nums, target):
	start, end = 0, len(nums) - 1
	while start+1 < end:
		mid = start + (end - start) // 2
		if target > nums[mid]:
			start = mid
		else:
			end = mid
	if nums[start] == target:
		return start
	elif nums[end] == target:
		return end
		
	return -1
	
	
	
## 2D binary search

def search_matrix(matrix, target):
	if not matrix:
		return False
	m = len(matrix)  # number of rows
	n = len(matrix[0])  #number of columns
	# find the start and end rows
	start, end = 0, m-1
	while start+1 < end:
		mid = start + (end - start) // 2
		if matrix[mid][0] >= target:
			end = mid
		else:
			start = mid
	if target > matrix[end][n-1] or target < matrix[start][0]:
		return False
	
	# case1: number in start row
	if matrix[start][n-1] >= target:
		left, right = 0, n-1
		while left+1 < right:
			mid = left + (right - left) // 2
			if matrix[start][mid] > target:
				right = mid
			else:
				left = mid
		if matrix[start][left] == target or matrix[start][right] == target:
			return True
		else:
			return False
			
	# case2: number in end row
	elif matrix[end][0] <= target:
		left, right = 0, n-1
		while left+1 < right:
			mid = left + (right - left) // 2
			if matrix[end][mid] > target:
				right = mid
			else:
				left = mid
		if matrix[end][left] == target or matrix[end][right] == target:
			return True
		else:
			return False
			
	# case3: number not in both rows
	elif target > matrix[start][n-1] and target < matrix[end][0]:
		return False
		
	return True
