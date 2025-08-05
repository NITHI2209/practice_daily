#04/08/2025
#question:
#Write a Python program to calculate the sum of only the positive numbers in a list.
#code:
Input = [4, -1, 2, -6, 7] 
count = 0
for i in Input:
    if i >=0:
        count += i
print(count)
