t=int(input())
for i in range(t):
    m=int(input())
    c=0
    for j in range (1,m):
        if(j*j==m):
            c+=1
    if(c==1):
        print('True')
    else:
        print('False')