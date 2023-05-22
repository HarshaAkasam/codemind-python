n=int(input())
a=list(map(int,input().split()))
m=max(a)
k=1
while(1):
    c=0
    for i in a:
        if((m*k)%i==0):
            c+=1
    if(c==n):
        break
    k+=1
print(m*k)