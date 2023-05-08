n=int(input())
p=n*n
s=0
while(p!=0):
    d=p%10
    p=p//10
    s=s+d
if(s==n):
    print('Neon Number')
else:
    print('Not Neon Number')