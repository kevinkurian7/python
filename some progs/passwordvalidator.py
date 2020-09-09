while True :
    print("enter your age please  :")
    age=input()
    if age.isdecimal():
        break
    print("please enter only a deciamal value")
while True:
    print("enter your password please  ")
    passw=input()
    if passw.isalnum():
        break
    print('please make sure tat the pass word has only leeters and numbers ')
