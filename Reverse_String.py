s=input()
for i in range(len(s)-1,-1,-1):
    if(s[i]==' '):
        c=0
        for j in range(i+1,len(s)):
            if(s[j]==' '):
                c+=1
            if(c==1):
                break
            else:
                print(s[j],end='')
        print(' ',end='')
    if(i==0):
        for j in range(0,len(s)):
            if(s[j]==' '):
                break
            print(s[j],end='')