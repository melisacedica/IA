#ex1

list=[1,2,3,4,5,6]

n=len(list)

mean=sum(list)/n
print(mean)

#ex2

list=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]

neg=[e for e in list if e<0]
poz=[e for e in list if e>=0]

print(neg)
print()
print(poz)

#ex3

list=[1,2,3,4,5,6]

print(list[0:-2])

#ex4

list=[1,2,3,4,5,6]

print(list[::2])

#ex5

list=[2,5,8,3,9,20]
n=[e for e in list if all(e<= a for a in list)]
print(n)