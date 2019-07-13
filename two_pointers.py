## two pointers of an array a = [1,3,4,5,5...], find two sum target.
def two_pointers(a, target):
    a.sort()
    left, right = 0, len(a)-1
    while left < right:
        if a[left] + b[right] == target:
            return [a[left], b[right]]
        elif a[left] + b[right] < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
