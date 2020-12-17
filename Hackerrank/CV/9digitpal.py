def prime(n):
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i +=  6
    return True

p=0
n=9999
a=[]
while(p<10):
    for i in range(9,-1,-1):
        num = str(n)
        pnum = num+str(i)+num[::-1]
        if(prime(int(pnum))):
            p+=1
            a.append(int(pnum))
    n=n-1
a.sort(reverse=True)
print(a)

# 9999  9999
# 
# 1000 9 1000