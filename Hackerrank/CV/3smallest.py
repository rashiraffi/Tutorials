n=[15,14,8,2,13,9,54,32,17]
s1=999997
s2=999998
s3=999999
for i in n:
    if(i<s3):
        if(i<s2):
            if(i<s1):
                s3=s2
                s2=s1
                s1=i
            else:
                s3=s2
                s2=i
        else:
            s3=i
print(s3)
