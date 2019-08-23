#! /usr/lib/python

# The general template for binary search is:
# - find mid
# - compare mid and target value to shrink the bound 
# - check if the result after the loop is qualified answer.

## Tips: when there is a certain range for the answer, the conditions to find left and right bound could be different.

## binary search a number 
def binary_search(nums, target):
	start, end = 0, len(nums) - 1
	while start + 1 < end:
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
	while start + 1 < end:
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
	
# search for a range: Given a sorted array of n integers, find the starting and ending position of a given target value.
# Keep an eye on the conditions when getting left and right bound. 
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            left_bound = start
        elif A[end] == target:
            left_bound = end 
        else:
            return [-1, -1]
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            right_bound = end
        elif A[start] == target:
            right_bound = start
        else:
            return [-1, -1]
            
        return [left_bound, right_bound]
