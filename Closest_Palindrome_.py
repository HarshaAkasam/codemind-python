def ip(n):
    if str(n)==str(n)[::-1]:
        return 1
    else:
        return 0
n=int(input())
for i in range(1,n):
    if(ip(n-i)==1 and ip(n+i)==1):
        print(n-i,end=' ')
        print(n+i,end=' ')
        break
    elif(ip(n-i)==1):
        print(n-i)
        break
    elif(ip(n+i)==1):
        print(n-i)
        break