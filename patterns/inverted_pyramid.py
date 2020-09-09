n=int(input())
for i in range(n,0,-1):
    try:
        for k in range(1,n+1-i):
            print(' ',end='')
    except:
        None
    for j in range(1,i+1):
        print('*',end='')
    try:
        for j in range(2,i+1):
            print('*',end='')
    except:
        None        
    print('')        

