def rev(a):
    r=0
    while(num!=0):
        n=num%10
        r=r*10+n
        num=num//10
    return r
num=int(input("enter the number:"))
rs=rev(num)
print(rs)
rev(a)