s=input()
m=0
for i in range(len(s)):
    c=0
    for j in range(i,len(s)-1):
        if(s[j]==s[j+1]):
            c+=1
        else:break
    if(m<c):m=c
print(m+1)