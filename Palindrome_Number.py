t=int(input())
for i in range (t):
    n=int(input())
    t=n
    s=0
    while(n!=0):
        d=n%10
        n=n//10
        s=s*10+d
    if(s==t):
        print('True')
    else:
        print('False')
    