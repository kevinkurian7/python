n=int(input())
for i in range(1,n+1):
    try:
        for k in range(1,n+1-i):
            print(' ',end='')
    except:
        None
    for j in range(1,i+1):
        print('*',end='')
    print('')                