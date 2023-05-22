def pan(n):
    t=n
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    if(s==t):
        return True
    return False
n=int(input())
if(pan(n)):
    print(True)
else:
    print(False)