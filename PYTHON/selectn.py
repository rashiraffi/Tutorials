from itertools import combinations 
  
# Get all combinations of [1, 2, 3] 
# and length 2 
comb = combinations([1, 2, 3], 2) 
  
# Print the obtained combinations 
for i in list(comb): 
    print(i)

def combo2(lst,n):
    if n==0:
        return [[]]
    l=[]
    for i in range(0,len(lst)):
        m=lst[i]
        remLst=lst[i+1:]
        for p in combo2(remLst,n-1):
            l.append([m]+p)
    return l
lst=(1,2,3,4,5,6,7,8,9)
cm=combo2(lst,3)
print(len(cm))
