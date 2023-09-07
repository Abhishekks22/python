n=int(input("enter the limit"))
a={2,5,7,9}
b=[]
for i in range(0,n):
    c=int(input("enter the numbers:"))
    b.append(c)
for i in b:
    a.add(i)
print(a)