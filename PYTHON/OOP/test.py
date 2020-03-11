a=[]
n=int(input())
s=input()
for i in range(0,n):
    a.append(int(s[i*2]))
s=int(input())
s=a[s-1]
a.sort()
print(a.index(s)+1)