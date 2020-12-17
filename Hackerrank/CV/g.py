def count(s):
    wres=0
    br=0
    w=1
    b=1
    for c in s:
        if(c=="w"):
            if(b==1):
                b=0
                w=1
            else:
                wres+=1
                b=1
                w=0
        elif(c=="b"):
            if(w==1):
                b=1
                w=0
            else:
                wres+=1
                b=0
                w=1
    w=1
    b=1
    for c in s:
        if(c=="b"):
            if(w==1):
                b=1
                w=0
            else:
                br+=1
                b=0
                w=1
        elif(c=="w"):
            if(b==1):
                b=0
                w=1
            else:
                br+=1
                b=1
                w=0
    if(wres<=br):
        return wres
    else:
        return br

s="wwwwwbbww"

if(s != "" and s[0]==s[-1]):
    f=0
    for i,c in enumerate(s):
        if(i>0 and c==s[i-1] and f==0 and c!=s[0]):
            f=i
    if(f==0):
        print(count(s))
    else:
        print(count(s[f:] + s[:f]))
else:
    if(s[0]=="w"):
        w=1
        b=1
        f=0
        for i,c in enumerate(s):
            if(c=="w" and f==0):
                if(b==1):
                    b=0
                    w=1
                else:
                    f=i
            elif(c=="b" and f==0):
                if(w==1):
                    b=1
                    w=0
                else:
                    f=i
        print(count(s[4:]+s[:4]))
    else:
        w=1
        b=1
        f=0
        for i,c in enumerate(s):
            if(c=="b" and f==0):
                if(w==1):
                    b=1
                    w=0
                else:
                    f=i
            elif(c=="w" and f==0):
                if(b==1):
                    b=0
                    w=1
                else:
                    f=i
        print(count(s[4:]+s[:4]))





        
