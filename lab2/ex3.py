n=int(input("Enter the number:"))
if(n%2)==1: ok=1
else: ok=0

if(ok==0):
   for i in range(n):
        print(i)

if(ok==1):
    for i in range(n):
        print(i*i)
