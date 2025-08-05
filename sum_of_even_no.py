#04/08/2025
#Write a Python program to calculate the sum of only the even numbers in a given list.
#code:
Input =[1, 2, 3, 4, 5, 6]  
count = 0
for i in Input:
    if i % 2 == 0:
        count += i
print(count)
