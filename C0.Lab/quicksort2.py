def quickSort(arr):
    if len(arr)==1:
        return arr
    p=arr[-1]
    left=[x for x in arr[:-1] if x<=p]
    right=[x for x in arr[:-1] if x>p]
    return quickSort(left) + [p] + quickSort(right)

res=quickSort([3,6,8,10,1,2,1])