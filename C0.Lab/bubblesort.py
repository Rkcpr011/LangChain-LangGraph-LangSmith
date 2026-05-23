# n=int(input().strip())
# arr=list(map(int , input().split()))

# def bubbleSort(arr):
#     swap=0
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1] , arr[j]
#                 swap=swap+1
#     print(f'total swap needed :', swap)
#     print(f'first element:', arr[0])
#     print(f'last element:' , arr[n-1])             
# bubbleSort(arr)


n = int(input().strip())
arr = list(map(int, input().split()))

swap = 0
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap += 1

print("Array is sorted in", swap, "swaps.")
print("First Element:", arr[0])
print("Last Element:", arr[-1])
