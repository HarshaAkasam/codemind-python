t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=[]
    for i in a:
        k.append(i)
    a.sort()
    if(k==a):
        print('0')
    else:
        print(max(a)-min(a))