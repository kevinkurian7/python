import  random 

n=random.randint(1,20)
flag=False
for i in range(9):
    guess=int(input("\n enter your guess"))
    if guess==n:
        print('\nyour guess was right ')
        flag=True
        break
    elif guess<n:
        print('\nyour guess is lower than the number')    
        continue
    elif guess>n:
        print('\nyour guess is greater than the number')    
        continue
if flag==False:
    print('\nyou failed to guess in 9 try')
elif flag==True:
    print('\nC-O-N-G-R-A-T-S')    