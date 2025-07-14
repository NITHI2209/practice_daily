#14/07/2025
#question:
#Write a function multiply(a, b) in two ways:
#1-One version prints the result.
#2-One version returns the result.
#code:
#1-
def multiplication_numbers(a,b):
    print(a*b)
multiplication_numbers(5,9)
#sample:
# 45
#2-
def multiplication_numbers(a,b):
    return a*b 

num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))
result = multiplication_numbers(num1,num2)
print(result)
#sample:
# enter the number 1: 5
# enter the number 2: 7
# 35
