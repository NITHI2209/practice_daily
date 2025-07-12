#12/07/2025
#question:
#Find the Factorial of a Number using function
#code:
def find_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i 
    return factorial

n = int(input("enter the number: "))
result = find_factorial(n)
print("factorial is",result)
#sample:
# enter the number: 5
# factorial is 120
