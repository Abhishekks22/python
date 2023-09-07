def listfunction():
    for i in range(0,n):
        c=int(input())
        a.append(c)
    for i in a:
        if i%2==0:
            b.append(i)
            a.remove(i)
            print("odd no",a)
            print("even",b)
n=int(input("enter the limit"))
a=[]
b=[]
listfunction()