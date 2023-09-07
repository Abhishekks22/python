n=input("Enter the string:")
a=['a','e','i','o','u']
b=[]
c=[]
l=len(n)
for i in range(l):
    if n[i] in a:
        b.append(n[i])
    else:
        c.append(n[i])
print(b)
print(c)
