#e1

def func(students):
    unique = sorted(set([n for name, n in students]))
    
    if len(unique) > 1:
        second = unique[1]
        
        sel = [name for name, n in students if n == second]
        
        sel.sort()
        
        for name in sel:
            print(name)
    else:
        print("Nu exista a doua cea mai mica nota")

clasa = [
    ['alex', 8.4],
    ['ionut', 9.3],
    ['mihai', 6.5],
    ['oana', 9.8],
    ['maria', 9.3]
]

func(clasa)
#e2

def Front3(l:str):
    if len(l)<=3:
        a=l
    elif len(l)>3:
        a=""
        for i in range(3):
            a+=l[i]
    return a*3

l='abcdefg'
print(Front3(l))

#e3

def consecutive(a,b):
    for i in range(len(a)-2):
        string=a[i:i+3]
        for j in range(len(b)-2):
            string2=b[j:j+3]

        if string==string2:
            return True
    return False


a=[1,2,3,4,5,6]
b=[5,6,1,2,3,4]

print(consecutive(a,b))

#e4

f=open("fisier.txt",'r')
d={}

def frecventa(f):
    try:
        with open("fisier.txt", 'r') as f:
            for linie in f:
                cuvinte = linie.split()
                
                for cuvant in cuvinte:
                    d[cuvant] = d.get(cuvant, 0) + 1
        return d
        
    except FileNotFoundError:
        print("Nu s-a putut deschide fisierul.")
        return -1

rezultat = frecventa("fisier.txt")
print(rezultat)

#e5

from collections import Counter

def frecventa(list, n):
    frecvente = Counter(list)
    
    mstcom = frecvente.most_common(n)
    
    print(f"Cele mai comune {n} elemente sunt:")
    for element, numar_aparitii in mstcom:
        print(f"{element}: {numar_aparitii} aparitii")

elemente_test = ['a', 'b', 'c', 'd', 'e', 'a', 'b']
n = 2

frecventa(elemente_test, n)

#e6
a=[1,2,3]
b=["a","b","c"]

for e1,e2 in zip(a,b):
    print(e1,e2)

#e7

def flatten(list_of_lists):
    return [el for sublist in list_of_lists for el in sublist]

lista = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = flatten(lista)

print(flattened)

#e8

class Generic_Form:
    def __init__(self,w,len):
        self.w=w
        self.len=len

    def getArea(self):
        return(self.w*self.len)

    def getPerimeter(self):
        return(2*self.w+2*self.len)

class Rectangle(Generic_Form):

    def __init__(self,width,height):
          self.width=width
          self.height=height
          super().__init__(width,height)

class Circle(Generic_Form):
    def __init__(self,radius,diameter):
        self.radius=radius
        self.diameter=diameter

    def getPerimeter(self):
        return(3.14*self.diameter)

    def getArea(self):
        return (2*3.14*self.radius)

rec=Rectangle(6,3)
gen=Generic_Form(2,5)
cir=Circle(3,8)
print(cir.getPerimeter())
print()
print(cir.getArea())

#e9

class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self,second):
        return(self.a+second.a,self.b+second.b)

    def sub(self,second):
        return(self.a-second.a,self.b-second.b)

    def mul(self,second):
        return(self.a*second.a,self.b*second.b)

no1=Complex(3,2)
no2=Complex(5,6)

print(no1.add(no2))
print()
print(no1.sub(no2))
print()
print(no1.mul(no2))
