def oddeven(*a):
    c=[]
    b=[]
    for i in a:
        if(i%2==0):
            b.append(i)
        else:
            c.append(i)
    print("evenlist",c)
    print("oddlist",b)
print(oddeven(1,2,3,4,5,6,7,8,9))