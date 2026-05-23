
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[9,8,7],[6,5,4],[3,2,1]]
res=[[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            res[i][j] += A[i][k] * B[k][j]
            
for row in res:
    for val in row:
        print(val)        
# print(res)

# print(*[12,12,1,2,3,4,5,6,7,9], sep='\n')