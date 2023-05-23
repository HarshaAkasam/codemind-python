s=input()
t,k=s,[]
s=list(set(s))
for i in s:
    k.append(t.count(i))
m=max(k)
while(m in k):
    k.remove(m)
if(len(k)>0):
    m=max(k)
    p=''
    for i in s:
        if(m==t.count(i)):
            p+=i
    p=''.join(sorted(p))
    print(p[0])
else:print('-1')