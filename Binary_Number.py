n=int(input())
a=[]
for i in range((2**n-1)+1):
    a.append(bin(i)[2:])
for i in a:
    while(len(i)<n):
        i='0'+i
    print(i)