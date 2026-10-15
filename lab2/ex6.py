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