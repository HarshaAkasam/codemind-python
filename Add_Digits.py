n=int(input())
def fun(n):
    s=0
    while(n):
        x=n%10
        s+=x
        n//=10
    return s
while(n>10):
    n=fun(n)
print(n)