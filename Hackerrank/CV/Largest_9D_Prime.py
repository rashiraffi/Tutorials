n=0
def prime(n):
    for k in range(2,int(n/2)):
        if(n%k==0):
            return False
    return True
num=9999
for i in range (9,-1,-1):
    while(num>1000 and n<3):
        print(num)
        if((num%1000)%2==0):
            num=int(str((num%1000)-1)+"999")
        else:
            num1=int(str(num)+str(i)+str(num)[::-1])
            if(prime(num1)):
                print(num1)
                n+=1
        num-=1