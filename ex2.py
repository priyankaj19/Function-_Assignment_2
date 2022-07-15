# WAP to find the sum of divisors of given number.

def sum_of_divisor(n):
    sum=0
    for i in range(1,n+1):
        if(n%i == 0):
            sum += i
    return sum
        
n = int(input("Enter the number: "))
print("Sum of divisors :",sum_of_divisor(n))