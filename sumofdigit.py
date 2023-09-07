def sum(n):
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n=n//10
    print(sum)
a=int(input("Enter the numbers  :"))
sum(a)
