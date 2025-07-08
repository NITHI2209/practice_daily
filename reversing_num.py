# 08/07/2025
num = input("Enter a number: ")
#reversing using string
print("Reversed number:", num[::-1])

# reversing number without using string
num = int(input("enter the number:  "))
reversed_num = 0
while num>0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
    
print("Reversed number is: " , reversed_num)
