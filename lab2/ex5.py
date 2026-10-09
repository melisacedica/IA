def func(s_in:str):
    s=""
    n=len(s_in)

    for i in range(n):
        s+=chr(ord(s_in[i])+1)

    return s

s_in=input("Enter the string:")
s=func(s_in)
print(s)
