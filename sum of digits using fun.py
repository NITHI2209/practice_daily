#16/07/2025
#question:
# Write a function that takes a number and returns the sum of its digits.
# Example:
# Input: 1234
# Output: 10 (1+2+3+4)
#code: using for loop
def find_sum_of_digit(a):
    sum_digit = 0
    for digit in str (a): #converting into string to separate each digit "1","2","3"..
        sum_digit += int(digit)
    return sum_digit

num = int(input("Enter the number: "))
result = find_sum_of_digit(num)
print("Sum of digits:", result)
#sample:
# Enter the number: 555789
# Sum of digits: 39

#code: using while loop
def find_sum_of_digit(a):
    sum_digit = 0
    while a > 0:
        sum_digit += a % 10
        a = a // 10
    return sum_digit

num = int(input("Enter the number: "))
result = find_sum_of_digit(num)
print("Sum of digits:", result)
