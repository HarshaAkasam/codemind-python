s=input()
m='a'
for i in s:
    if(ord(i)>ord(m)):
        m=i
print(m)