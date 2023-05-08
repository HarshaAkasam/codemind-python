n,m=map(int,input().split())
if(n>m):
    t=n
else:
    t=m
i=1
while (i!=0):
    if((i*t)%m==0 and (i*t)%n==0):
        print(i*t)
        break
    i+=1