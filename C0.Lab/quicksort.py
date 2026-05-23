def quick_sort(arr):
    if len(arr) <= 1:  # Base case: already sorted
        return arr
    
    pivot = arr[-1]  # Choosing last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements <= pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements > pivot
    
    return quick_sort(left) + [pivot] + quick_sort(right)
res=quick_sort([3, 6, 8, 10, 1, 2, 1])
print(res)