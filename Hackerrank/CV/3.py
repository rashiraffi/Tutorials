string = input()
substring = input()

def find(s,ss):
    p=1
    m=b=0
    s_l = len(s)
    ss_l = len(ss)
    if(s_l == ss_l):
        return 1
    i=s.index(ss)
    if(i==0):
        b= s_l - ss_l
        return (p+b)
    else:
        b = (s_l-(i+ss_l)) + i
        m += (2*ss_l)
        return(p+b+m)
substrig_of_substring = [substring[i: j] for i in range(len(substring)) for j in range(i + 1, len(substring) + 1)] 

def delsubstring(s,ss):
    i=s.index(ss)
    l_ss=len(ss)
    return (s[:i] + s[i+l_ss:])

def sortbylength(string, length): 
    for i in range(1, length): 
        temp = string[i] 
  
        j = i - 1
        while j >= 0 and len(temp) < len(string[j]): 
            string[j + 1] = string[j] 
            j -= 1
  
        string[j + 1] = temp
sortbylength(substrig_of_substring,len(substrig_of_substring))
n=0
for _ in substrig_of_substring[::-1]:
    while(_ in string):
        n += find(substring,_)
        string = delsubstring(string,_)

print(n)

    
    
 