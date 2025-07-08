# using string 
num = input("enter the number: ")
if num == num[::-1]:
    print(f"{num} is a palinrome")
else:
    print(f"{num} is not palinrome")
# without using string
num = int(input("enter the number: "))
reversed_num = 0 
original_num = num 
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original_num == reversed_num:
     print(f"{original_num} is a palinrome")
else:
    print(f"{original_num} is not palinrome")
