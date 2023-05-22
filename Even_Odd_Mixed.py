n=int(input())
s=0
x=0
c=0
while(n!=0):
    d=n%10
    n=n//10
    x+=1
    if(d%2==0):
        c+=1
    else:
        s+=1
if(x==c):
    print('Even')
elif(x==s):
    print('Odd')
elif(s!=0 and c!=0):
    print('Mixed')