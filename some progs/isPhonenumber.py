
#program only for checking indian number
def isPhoneNumber(phoneno):
    if len(phoneno)!=13:
   
        return False 
       
    elif phoneno[0:3]!="+91":
         
         return False
       
    for i in range(1,len(phoneno)):
        if not phoneno[i].isdecimal():
        
            return False
         
    return True      
phoneno=input('enter the numbere')

print(isPhoneNumber(phoneno))
