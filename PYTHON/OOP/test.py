def solution (R, L):
    a=set()
    for i in range (L,R+1):
        for j in range (0,i):
            if(i%j==0):
                if(i not in a):
                    a.add(i)

    return i
p=solution(4,2)
print(p)