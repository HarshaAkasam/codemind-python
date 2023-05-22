n,m=map(int,input().split())
for i in range (1,m+1):
    if(i%2!=0):
        print(n,'x',i,'=',n*i)
        