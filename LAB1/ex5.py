list=[2,5,8,3,9,20]
n=[e for e in list if all(e<= a for a in list)]
print(n)