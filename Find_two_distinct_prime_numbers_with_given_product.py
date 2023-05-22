def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=0
for i in range(2,n):
    for j in range(2,n):
        if(i*j==n and prime(i) and prime(j)):
           print(i,j)
           c=1
           break
    if(c==1):
        break
if(c==0):
    print('-1')

    