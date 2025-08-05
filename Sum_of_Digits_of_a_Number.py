#04/08/2025
#question
#Write a Python program to find the sum of all digits in a given number
#code:
Input = 1234
count = 0  
digit = list(map(int,str(Input)))
for i in digit:
    count += i
print(count)
