#15/07/2025
#question:
#Function to check if a number is a perfect number
#A perfect number is a number that is equal to the sum of its proper divisors (excluding the number itself).
#code:
def is_perfect_number(n):
    sum_divisor = 0 
    for i in range(1,n):
        if n%i ==0:
            sum_divisor += i 
    if sum_divisor==n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")
num = int(input("enter the number: "))
is_perfect_number(num)
#sample:
#1) enter the number: 6
# 6 is a perfect number
#2) enter the number: 7
# 7 is not a perfect number
