n=int(input())
t=n
c=0
x=0
while(n):
    d=n%10
    a=t
    s=0
    while(a):
        if(d==a%10):
            s+=1
        a//=10
    if(s==1):
        c+=1
    n//=10
    x+=1
if(x==c):
    print('Unique Number')
else:
    print('Not Unique Number')
            