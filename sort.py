# common sort algorithms

# Bubble Sort: compare the two adjacent number and make the larger one "float"

def bubbleSort(array):
    if not array:
        return array
    
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
    
# Merge Sort: split into two parts and use recursion

def mergeSort(array):
    if len(array) == 1:
        return array
    n = len(array)
    left = array[:n//2]
    right = array[n//2:]
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
    
#  Insertion Sort: insert the new element into the sorted part 
def insertionSort(array):
    for i in range(1, len(array)):
        j = i-1
        next_element = array[i]
        while array[j] > next_element and j >= 0:
            array[j+1] = array[j]
            j = j - 1
        
        array[j+1] = next_element
        
        
        
#  Quick Sort:         
