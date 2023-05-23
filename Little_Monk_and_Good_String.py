s=input()
a='aeiou'
m=0
for i in range(len(s)):
    k=''
    if(s[i] in a):
        k+=s[i]
        for j in range(i+1,len(s)):
            if s[j] in a:
                k+=s[j]
            else:
                break
        if(m<len(k)):
            m=len(k)
print(m)