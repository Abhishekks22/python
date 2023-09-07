try:
    num= int(input("enter the number:"))
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
except ValueError:
    raise ValueError("invalid input.please enter a valid integer")
