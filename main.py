#ex1

price={"apples":10,"milk":12,"bread":5}
mylist=[("apples",2),("milk",2)]
price.values()
sum=price.get("apples")*mylist[0][1]+price.get("milk")*mylist[1][1]
print(sum)

#ex2

friends=[("andrew",10),("george",20),("andrew",5),("ann",10)]
setp=set()
for nume,suma in friends:
    setp.add(nume) 

print(setp)

#ex3

n=int(input("Enter the number:"))
if(n%2)==1: ok=1
else: ok=0

if(ok==0):
   for i in range(n):
        print(i)

if(ok==1):
    for i in range(n):
        print(i*i)

#ex4

n_in=int(input("Enter the number: "))
s_in=input("Enter the string: ")

d={}

for i in range(n_in):
    d[i]=s_in[i]

print(d)

#ex5

def func(s_in:str):
    s=""
    n=len(s_in)

    for i in range(n):
        s+=chr(ord(s_in[i])+1)

    return s

s_in=input("Enter the string:")
s=func(s_in)
print(s)

#ex6

f=open('test.txt',"r")
f2=open('test2.txt',"w")
text=f.readline()

while text:
   if len(text)>0:
        text=chr(ord(text[0])-32)+text[1:]

        f2.write(text)
        text=f.readline()

f.close()
f2.close()