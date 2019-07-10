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
		
