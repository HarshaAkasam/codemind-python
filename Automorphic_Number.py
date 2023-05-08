n=int(input())
s=str(n**2)
c=0
t=n
k=''
while(n):
    c+=1
    n//=10
for i in range(len(s)-1,len(s)-c-1,-1):
    k+=s[i]
f=''
for i in range(len(k)-1,-1,-1):
    f+=k[i]
if((f)==str(t)):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')