def vote(a):
    if a>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
a=int(input("enter the age:"))
vote(a)