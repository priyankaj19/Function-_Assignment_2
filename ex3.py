# WAP to check given number is a perfect number or not.

def perfect(n):
    sum = 0
    for i in range(1,n):
        if (n%i == 0):
            sum += i
    if (n==sum):
        print(n,"is a perfect number.")
    else:
        print(n,"is not a perfect number.")

n = int(input("Enter the number: "))
perfect(n)