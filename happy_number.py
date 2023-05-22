def su(n):
    s=0
    while(n):
        s+=((n%10)**2)
        n//=10
    return s
def dc(n):
    c=0
    while(n):
        n//=10
        c+=1
    return c
n=int(input())
if(dc(n)==1):
    if(n==1 or n==7):
        print(True)
else:
    while(1):
        s=su(n)
        if(dc(s)==1 and s==1 or s==7):
            print(True)
            break
        elif(dc(s)==1 and s!=1 and s!=7):
            print(False)
            break
        n=s
        
    