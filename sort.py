# sort algorithms

# Bubble Sort: compare the two adjacent number and make the larger one "float"

def bubbleSort(array):
    if not array:
        return array
    
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
    
# Merge Sort: split into two parts and use recursionn O(nlogn)

def mergeSort(array):
    if len(array) == 1:
        return array
    n = len(array)
    left = array[:n // 2]
    right = array[n // 2:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result = result + left
    if right:
        result = result + right
    return result
    
#  Insertion Sort: insert the new element into the sorted part. O(n^2)

def insertionSort(array):
    for i in range(1, len(array)):
        j = i-1
        next_element = array[i]
        while array[j] > next_element and j >= 0:
            array[j+1] = array[j]
            j = j - 1
        
        array[j+1] = next_element
        
        
        
#  Quick Sort: pick a pivot and let the left side smaller than the pivot and the other side larger and repeat for the left side and right side until the the whole array is sorted. O(nlogn)

	# partition part is usually used in solving array problems like Find Kth Largest Number, it is a quick select method. 
def quickSort(array, low, high):
    if low > high: return 
    pivot_location = partition(array, low, high)
    quickSort(array, low, pivot_location - 1)
    quickSort(array, pivot_location + 1, high)


def partition(array, low, high):
    pivot = array[high]
    index = low
    for i in range(low, high):
        if array[i] < pivot: 
            array[i], array[low] = array[low], array[i]
            index = index + 1
    array[index], array[high] = array[high], array[index]
    return index
	
	## version 2 find the kth smallest element
def QuickSort(array, start, end, k):
	if left == right:
		return array[k]
	left, right = start, end
	pivot = array[start + (start - end) // 2]
	while left <= right:
		while left <= right and array[left] < array[pivot]:
			left += 1
		while left <= right and array[right] > array[pivot]:
			right -= 1
		if left <= right:
			array[left], array[right] = array[right], array[left]
			left += 1 
			right -= 1
	if k <= right:
		return QuickSort(array, start, right, k)
	if k >= left:
		return QuickSort(array, left, end, k)
	return array[k]



