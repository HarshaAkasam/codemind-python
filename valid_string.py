s=input()
a,t=[],s
for i in s:
    a.append(s.count(i))
b=list(set(a))
#print()
x=[]
for i in b:
    x.append(a.count(i))
if(len(x)>2):
    print('Not Valid')
elif(len(x)<2):
    print('Valid String')
else:
    if(x[0]==1 or x[1]==1):
        print('Valid String')
    else:
        print('Not Valid')