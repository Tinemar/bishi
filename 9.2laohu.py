from collections import deque
count = 0
def result(nums):
    mergesort(nums)
    return count
def mergesort(nums):
    if len(nums)<=1:
        return nums
    length = len(nums)
    left = mergesort(nums[0:length//2])
    right = mergesort(nums[length//2:])
    return merge(left,right)
def merge(left,right):
    global count
    merged = deque()
    left = deque(left)
    right = deque(right)
    while left and right:
        if left[0]<=right[0]:
            merged.append(left.popleft())
        else:
            count += len(left)
            merged.append(right.popleft())
    if right:
        merged.extend(right)
    else:
        merged.extend(left)
    return merged
print(result([9,1,0,5,4]))