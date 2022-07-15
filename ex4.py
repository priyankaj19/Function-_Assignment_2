# WAP to print perfect numbers in given range.

def perfect(n1,n2):
    print("All perfect numbers in given range: ")
    for j in range(n1,n2+1):
        sum = 0
        for i in range(1,j):
            if (j%i == 0):
                sum += i
        if (j==sum):
            print(j,end=" ")

n1 = int(input("Enter start range value: "))
n2 = int(input("Enter end range value: "))
perfect(n1,n2)