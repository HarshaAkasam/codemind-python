n=int(input())
n=list(str(n))
i=0
while(i<len(n)):
    if(n[i]=='6'):
        n[i]='9'
        break
    i+=1
for i in n:
    print(i,end='')