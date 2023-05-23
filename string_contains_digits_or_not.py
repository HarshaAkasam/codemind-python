t=int(input())
for i in range(t):
    s=input()
    c='1234567890'
    for i in s:
        if i in c:
            print('Yes')
            break
    else:
        print('No')
            
    