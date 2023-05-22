def pan(n):
    t=n
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    if(s==t):
        return 1
    return 0
def rev(n):
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    return s
n=int(input())
while(1):
    n=n+rev(n)
    if(pan(n)):
        print(n)
        break
    