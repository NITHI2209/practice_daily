# 08/07/2025
# using for loop
n =  int(input("enter the number: "))
factorial = 1
for i in range(1,n+1):
        factorial = factorial * i

print(f" {n} factorial = {factorial}")

# using while loop
n = int(input("enter the number: "))
factorial =  1 
i = 1 
while i <= n:
    factorial =  factorial * i 
    i += 1 
print(f" {n} factorial = {factorial}")
