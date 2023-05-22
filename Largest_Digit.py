n=int(input())
s=0
while(n):
    if(s<(n%10)):
        s=n%10
    n//=10
print(s)