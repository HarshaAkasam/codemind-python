t=int(input())
for i in range(t):
    n=int(input())
    s=1
    while(n!=1):
        s*=n
        n=n-1
    print(s)
    