def maxSubarray(arr):
    cs=arr[0]
    ms=arr[0]
    for i in range(1,len(arr)):
        cs=max(arr[i],cs+arr[i])
        ms=max(cs,ms) 
    if all(x<0 for x in arr):
        sum_subseq=max(arr)
    else:    
        sum_subseq=sum(x for x in arr if x>0)    
            
    return ms,sum_subseq  
res,res2=maxSubarray([-1, -2, -3, -4, -5])
print(res,res2)

# def maxSubarray(arr):
#     max_current = max_global = arr[0]
#     for num in arr[1:]:
#         max_current = max(num, max_current + num)
#         max_global = max(max_global, max_current)
#     max_subseq = sum(x for x in arr if x > 0) if any(x > 0 for x in arr) else max(arr)
#     return [max_global, max_subseq]
# res, res2 = maxSubarray([-1, -2, -3, -4, -5])
# print(res, res2)