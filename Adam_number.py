def rev(n):
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    return s

n=int(input())
r=rev(n)
s=n*n
a=r*r
k=rev(s)
if(k==a and n==rev(r)):
    print(True)
else:
    print(False)