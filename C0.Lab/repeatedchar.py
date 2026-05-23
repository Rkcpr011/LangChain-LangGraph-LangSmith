# def repeatedchar(s,n):
#     repeated=''
#     for i in range(0,n):
#         repeated=repeated+s[i%len(s)]
#     res=repeated.count('a')    
#     print(res) 
#     print(repeated) 
# repeatedchar('aba',100)

s='aba'
n=100
valucountInOneTerm=s.count('a')
full_term=n//len(s)
partial_term=n%len(s)
res=valucountInOneTerm*full_term+s[0:partial_term].count('a')
print(res)


#     str2=s*4
#     res=[]
#     for x in s:
#         res.append(x)
#     print(res)  



# n=3
# res2=res[0:n+1]
# COUNT=res.count('a')
# print(COUNT)
# print(res2 )
# print(str2)
