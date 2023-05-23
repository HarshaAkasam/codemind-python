s=input()
v='aeiouAEIOU'
c='QWRTYPSDFGHJKLMZNXBCVqwrtyplkjsjhgdfzxcvbnm'
i,t=0,''
while(i<len(s)):
    if(s[i] in v):t+='V'
    elif(s[i] in c):t+='C'
    i+=1
i=0
j=0
s=t[0]
while(i<len(t)):
    if(t[i]!=s[j]):
        s+=t[i]
        j+=1
    i+=1
print(s)