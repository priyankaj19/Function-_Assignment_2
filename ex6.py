# WAP to check if given number is perfect square or not.

def perfect_number(n):
    import math
    r=int(math.sqrt(n))
    if (r**2 == n):
        print(n,"is a perfect square.")
    else:
        print(n,"is not a perfect square.")

n=int(input("Enter the number: "))
perfect_number(n)