price={"apples":10,"milk":12,"bread":5}
mylist=[("apples",2),("milk",2)]
price.values()
sum=price.get("apples")*mylist[0][1]+price.get("milk")*mylist[1][1]
print(sum)