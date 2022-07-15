# WAP to check if given number is fibonacci number or not.

def fibonacci_number(n):
    import math
    r1=int(math.sqrt(5*(n**2) + 4))
    r2=int(math.sqrt(5*(n**2) - 4))
    # print(r1,r2)                     # to check r1,r2
    # print((5*(n**2) + 4),(5*(n**2) - 4))
    if ((r1**2 == (5*(n**2) + 4)) or (r2**2 == (5*(n**2) - 4))):
        print(n,"is a fibonacci number.")
    else:
        print(n,"is not a fibonacci number.")

n=int(input("Enter the number: "))
fibonacci_number(n)