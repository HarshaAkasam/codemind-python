n=int(input())
t=n
s=0
while(n!=0):
    d=n%10
    n=n//10
    p=1
    for i in range (1,d+1):
        p=p*i
    s=s+p
if(s==t):
    print('The number',s,'is a strong number')
else:
    print('The number',t,'is not a strong number')