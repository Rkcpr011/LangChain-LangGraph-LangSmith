def rotate_list(lst, k):
    res=[]
    for i in range(k+1,len(lst),1):
        res.append(lst[i]) 
    for j in range(0,k+1,1):
        res.append(lst[j])
    return res    
        
print(rotate_list([1,2,3,4,5],2))