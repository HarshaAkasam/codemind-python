n=int(input())
p=1
s=0
while(n):
    s+=(n%10)
    p*=(n%10)
    n//=10
if(s==p):
    print('Spy Number')
else:
    print('Not Spy Number')