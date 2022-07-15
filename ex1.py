# WAP to find all divisors of given number.

def divisor(n):
    print("Divisors of n",n,":")
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")

n = int(input("Enter the number: "))
divisor(n)