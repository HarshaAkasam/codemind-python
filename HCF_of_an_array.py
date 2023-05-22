n=int(input())
a=list(map(int,input().split()))
m=min(a)
for i in range(m,0,-1):
    for j in a:
        if(j%i!=0):
            break
    else:
        print(i)
        break