string = input()
substring = input()
result=0
def find(string,substring):
    p=1
    m=b=0
    i=0
    s_l = len(string)
    ss_l = len(substring)
    if(s_l == ss_l):
        return 1
    i=string.index(substring)
    if(i==0):
        b= s_l - ss_l
        return (p+b)
    else:
        b = (s_l-(i+ss_l)) + i
        m += (2*ss_l)
        return(p+b+m)

def delsubstring(s,ss):
    i=s.index(ss)
    l_ss=len(ss)
    return (s[:i] + s[i+l_ss:])

n=len(substring)
for i in range(0,n):
    f=0
    l=n-i
    while(l<=n):
        if(substring[f:l] in string):
            r=find(substring,substring[f:l])
            while(substring[f:l] in string):
                result += r
                string = delsubstring(string,substring[f:l])
        l+=1
        f+=1

print(result,end="")