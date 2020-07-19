import re
f=input("enter the file name :  ")
try:
   fhand=open('regex.txt')

    
except :
    print("error")   

numlist=[]
for line in fhand:
    line=line.strip()
    numlist.append((sum([int(s) for s in re.findall('[0-9]+',line)])))
    

   # x=re.findall('[0-9]+',line)
   # if len(x)==0:
    #    continue
    #num=int(x[0])
   # numlist.append(num)
print(sum(numlist))




